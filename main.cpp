#include <iostream>
#include <cstring>
#include <cassert>

void hybrid_test(const char *, const char *, const char *,
                 const char *, const char *,
                 const char *, const char *, const char *,
                 const char *, const char *, const char *,
                 const char *, const char *,
                 const int, const int, const int, const int, const int, const int,
                 const int, const int, const int, const int, const int, const int);

//void deep_test10M();
void hnsw_test( const char *,
                const char *, const char *,
                const char *, const char *, const char *, const char *,
                const char *, const char *, const char *,
                const int, const int, const int, const int, const int, const int, const int);


void usage(const char * cmd)
{
    printf ("Usage: %s [options]\n", cmd);

    printf (
            "  Input\n"
                    "  Path parameters\n"
                    "    -path_data filename     set of base vectors (bvecs file format)\n"
                    "    -path_edges filename     set of links in the constructed graph  (ivecs file format)\n"
                    "    -path_info filename     set of graph parameters)\n"
                    "    -path_gt filename     groundtruth (ivecs file format)\n"
                    "    -path_q filename     set of queries (ivecs file format)\n"
                    "    -path_codebooks filename     codebook for PQ vectors (fvecs file format)\n"
                    "    -path_tables filename     precomputed distances for PQ vectors (dat file format)\n"
                    "  General parameters\n"
                    "    -n #            use n points from the file, default: 1B\n"
                    "    -d #            dimension of the vector, default: 128\n"
                    "    -k #            number of NN to search, default: 1\n"
                    "    -M #            number of mandatory links maxM0 = 2*M, default: M=4\n"
                    "    -nq #           number of queries, default: 10000\n"
                    "    -efConstruction #            -//-, default: 240\n"
                    "    -l2space int / float            Choose int for PQ compressed data or integer datasets like SIFT\n"
                    "                                    Choose float for real datasets like DEEP\n"
    );
    exit (0);
}


int main(int argc, char **argv) {
    size_t vecsize = 1000000000;
    size_t qsize = 10000;
    size_t vecdim = 128;
    size_t M = 4;
    size_t efConstruction = 240;
    size_t ncentroids;
    size_t nsubcentroids;
    size_t efSearch = 240;
    size_t M_PQ = 16;
    size_t nprobes = 64;
    size_t max_codes = 10000;


    const char *path_gt = NULL;
    const char *path_q = NULL;
    const char *path_data = NULL;
    const char *path_codebooks = NULL;
    const char *path_tables = NULL;
    const char *path_edges = NULL;
    const char *path_info = NULL;

    const char *path_index = NULL;
    const char *path_precomputed_idxs = NULL;
    const char *path_pq = NULL;
    const char *path_norm_pq = NULL;
    const char *path_learn = NULL;
    const char *path_centroids = NULL;

    const char *path_groups;
    const char *path_idxs;

    const char *l2space_type = NULL; //{int, float, new_pq}
    int k = 1, ret, ep;

    if (argc == 1)
        usage (argv[0]);

    for (int i = 1 ; i < argc ; i++) {
        char *a = argv[i];

        if (!strcmp (a, "-h") || !strcmp (a, "--help"))
            usage (argv[0]);

        /** Paths **/
        if (!strcmp (a, "-path_codebooks") && i+1 < argc) {
            path_codebooks = argv[++i];
        }
        else if (!strcmp (a, "-path_tables") && i+1 < argc) {
            path_tables = argv[++i];
        }
        else if (!strcmp (a, "-path_data") && i+1 < argc) {
            path_data = argv[++i];
        }
        else if (!strcmp (a, "-path_info") && i+1 < argc) {
            path_info = argv[++i];
        }
        else if (!strcmp (a, "-path_edges") && i+1 < argc) {
            path_edges = argv[++i];
        }
        else if (!strcmp (a, "-path_q") && i+1 < argc) {
            path_q = argv[++i];
        }
        else if (!strcmp (a, "-path_gt") && i+1 < argc) {
            path_gt = argv[++i];
        }
        else if (!strcmp (a, "-path_pq") && i+1 < argc) {
            path_pq = argv[++i];
        }
        else if (!strcmp (a, "-path_norm_pq") && i+1 < argc) {
            path_norm_pq = argv[++i];
        }
        else if (!strcmp (a, "-path_precomputed_idx") && i+1 < argc) {
            path_precomputed_idxs = argv[++i];
        }
        else if (!strcmp (a, "-path_index") && i+1 < argc) {
            path_index = argv[++i];
        }
        else if (!strcmp (a, "-path_learn") && i+1 < argc) {
            path_learn = argv[++i];
        }
        else if (!strcmp (a, "-path_centroids") && i+1 < argc) {
            path_centroids = argv[++i];
        }
        else if (!strcmp (a, "-path_groups") && i+1 < argc) {
            path_groups = argv[++i];
        }
        else if (!strcmp (a, "-path_idxs") && i+1 < argc) {
            path_idxs = argv[++i];
        }
        /** Int Parameters **/
        else if (!strcmp (a, "-k") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &k);
            assert (ret);
        }
        else if (!strcmp (a, "-efConstruction") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &efConstruction);
            assert (ret);
        }
        else if (!strcmp (a, "-d") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &vecdim);
            assert (ret);
        }
        else if (!strcmp (a, "-n") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &vecsize);
            assert (ret);
        }
        else if (!strcmp (a, "-nq") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &qsize);
            assert (ret);
        }
        else if (!strcmp (a, "-M") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &M);
            assert (ret);
        }
        else if (!strcmp (a, "-l2space") && i+1 < argc) {
            l2space_type = argv[++i];
        }
        else if (!strcmp (a, "-nc") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &ncentroids);
            assert (ret);
        }
        else if (!strcmp (a, "-M_PQ") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &M_PQ);
            assert (ret);
        }
        else if (!strcmp (a, "-efSearch") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &efSearch);
            assert (ret);
        }
        else if (!strcmp (a, "-nprobes") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &nprobes);
            assert (ret);
        }
        else if (!strcmp (a, "-max_codes") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &max_codes);
            assert (ret);
        }
        else if (!strcmp (a, "-nsubcentroids") && i+1 < argc) {
            ret = sscanf (argv[++i], "%d", &nsubcentroids);
            assert (ret);
        }
    }

    if ((!path_codebooks && path_tables) || (path_codebooks && !path_tables)) {
        std::cerr << "Enter path_codebooks and path_tables to use PQ" << std::endl;
        exit(1);
    }

    //if (strcmp (l2space_type, "int") && strcmp (l2space_type, "float")) {
    //    std::cerr << "Available l2space: float or int" << std::endl;
    //    exit(1);
    //}

//    hnsw_test(l2space_type,
//              path_pq, path_learn,
//              path_codebooks, path_tables, path_data, path_q,
//              path_gt, path_info, path_edges,
//              k, vecsize, qsize, vecdim, efConstruction, M, M_PQ);

    hybrid_test(path_centroids, path_index, path_precomputed_idxs,
                path_pq, path_norm_pq, path_learn, path_data, path_q,
                path_gt, path_info, path_edges,
                path_groups, path_idxs,
                k, vecsize, ncentroids, qsize, vecdim, efConstruction, efSearch, M,
                M_PQ, nprobes, max_codes, nsubcentroids);


    return 0;  
};
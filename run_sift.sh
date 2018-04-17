#!/bin/bash

################################
# HNSW construction parameters #
################################

M="16"                # Min number of edges per point
efConstruction="500"  # Max number of candidate vertices in priority queue to observe during construction

###################
# Data parameters #
###################

nb="1000000"          # Number of base vectors
nq="10000"            # Number of queries
ngt="100"             # Number of groundtruth neighbours per query

d="128"               # Vector dimension

#####################
# Search parameters #
#####################

k="100"                 # Number of the closest vertices to search
efSearch="500"         # Max number of candidate vertices in priority queue to observe during searching

#########
# Paths #
#########

path_data="${PWD}/data/mysift"
path_model="${PWD}/models/mysift"

path_base="${path_data}/mysift_base.fvecs" #triplet_answers.fvecs"
path_gt="${PWD}/data/sift/sift_groundtruth.ivecs"
path_q="${path_data}/mysift_queries.fvecs"

path_edges="${path_model}/hnsw_M${M}_ef${efConstruction}.ivecs"
path_info="${path_model}/hnsw_M${M}_ef${efConstruction}.bin"

#######
# Run #
#######
${PWD}/main -M ${M} \
                     -efConstruction ${efConstruction} \
                     -n ${nb} \
                     -nq ${nq} \
                     -ngt ${ngt} \
                     -d ${d} \
                     -k ${k} \
                     -efSearch ${efSearch} \
                     -path_data ${path_base} \
                     -path_gt ${path_gt} \
                     -path_q ${path_q} \
                     -path_edges ${path_edges} \
                     -path_info ${path_info} \
                     -l2space "float"
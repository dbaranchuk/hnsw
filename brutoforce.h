#pragma once
#include <string.h>
namespace hnswlib {
	template <typename dist_t> class BruteforceSearch {
	public:
		BruteforceSearch(SpaceInterface<dist_t> *s) {

		}
		BruteforceSearch(SpaceInterface<dist_t> *s, size_t maxElements) {
			maxelements_ = maxElements;

			space = s;
			data_size_= s->get_data_size();
			cout << data_size_ << "\n";
			size_per_element_ = data_size_ + sizeof(labeltype);
			data_=(char *)malloc(maxElements*size_per_element_);
			cur_element_count = 0;
		}
		~BruteforceSearch() {
			free(data_);
		}

		SpaceInterface<dist_t> *space;
		char *data_;
		size_t maxelements_;
		size_t cur_element_count;
		size_t size_per_element_;

		size_t data_size_;

		void addPoint(void *datapoint, labeltype label) {
			
			if (cur_element_count >= maxelements_)
			{
				cout << "The number of elements exceeds the specified limit\n";
				throw exception();
			};
			memcpy(data_ + size_per_element_*cur_element_count+ data_size_, &label, sizeof(labeltype));
			memcpy(data_ + size_per_element_*cur_element_count, datapoint, data_size_);
			cur_element_count++;
		};
		std::priority_queue< std::pair< dist_t, labeltype >> searchKnn(void *query_data,int k) {
			std::priority_queue< std::pair< dist_t, labeltype >> topResults;
			for (int i = 0; i < k; i++) {
				dist_t dist = space->fstdistfunc(query_data, data_ + size_per_element_*i);
				topResults.push(std::pair<dist_t, labeltype>(dist, *((labeltype*)(data_ + size_per_element_*i + data_size_))));
			}
			dist_t lastdist= topResults.top().first;
			for (int i = k; i < cur_element_count; i++) {
				dist_t dist=space->fstdistfunc(query_data, data_ + size_per_element_*i);
				if(dist < lastdist) {				
					topResults.push(std::pair<dist_t, labeltype>(dist,*((labeltype*) (data_ + size_per_element_*i + data_size_))));
					if (topResults.size() > k)
						topResults.pop();
					lastdist = topResults.top().first;
				}

			}
			return topResults;
		};
	};
}

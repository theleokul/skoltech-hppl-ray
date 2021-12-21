from time import perf_counter

from skimage import data, filters
import ray



def do_smth_crazy(num_iter, image):
    for _ in range(num_iter):
        _ = filters.sobel(image)
        
        
if __name__ == '__main__':
    image = data.coins()
    
    counter = 10000
    
    start = perf_counter()
    ray.init(num_cpus=4, include_dashboard=True)
    remote_do_smth_crazy = ray.remote(do_smth_crazy)
    ray.get([remote_do_smth_crazy.remote(counter, image) for _ in range(4)])
    end = perf_counter()
    print('parallel: ', end - start)
    
    start = perf_counter()
    do_smth_crazy(4 * counter, image)
    end = perf_counter()
    print('simple: ', end - start)
    
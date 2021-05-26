# python3

from collections import namedtuple
import queue

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:

    def __init__(self, size):
        self.size = size
        self.pending = queue.Queue(maxsize=self.size)
        self.finish_time = queue.Queue()
        self.last_finish = 0

    def print_queue(self, que):
        for n in list(que.queue):
            print(n, end=" ")
        print("\n")

    def process(self, request, verbose=False):
        if (self.pending.empty() == False):
            finish_count = 0
            for fin_time in list(self.finish_time.queue):
                if fin_time <= request.arrived_at:
                    finish_count += 1
            for _ in range(finish_count):
                self.pending.get()
        
        if verbose:
            self.print_queue(self.pending)

        is_dropped = self.pending.full()
        started_at = -1 if is_dropped else max(request.arrived_at, self.last_finish)

        if is_dropped == False:
            self.pending.put(request)
            self.last_finish = max(request.arrived_at, self.last_finish) + request.time_to_process
            self.finish_time.put(self.last_finish)
        
        if verbose:
            self.print_queue(self.pending)
            self.print_queue(self.finish_time)
            print(Response(is_dropped, started_at))

        return (Response(is_dropped, started_at))      

def process_requests(requests, buffer, verbose=False):
    responses = []
    for request in requests:
        responses.append(buffer.process(request, verbose=verbose))
    return responses

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer, verbose=False)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

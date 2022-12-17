'''
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.

'''

import heapq


class StockPrice:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.price_count = {}
        self.price_at_time = {}
        self.latest_time = 0

    def re_heap(self):
        while self.max_heap and -self.max_heap[0] not in self.price_count:
            heapq.heappop(self.max_heap)
        while self.min_heap and self.min_heap[0] not in self.price_count:
            heapq.heappop(self.min_heap)

    def update(self, timestamp: int, price: int) -> None:
        self.latest_time = max(self.latest_time, timestamp)
        if timestamp in self.price_at_time:
            old_price = self.price_at_time[timestamp]
            self.price_count[old_price] -= 1
            if self.price_count[old_price] == 0:
                del self.price_count[old_price]
                self.re_heap()
        self.price_at_time[timestamp] = price
        self.price_count[price] == self.price_count.get(price, 0) + 1
        heapq.heappush(self.max_heap, -price)
        heapq.heappush(self.min_heap, price)

    def current(self) -> int:
        return self.price_at_time[self.latest_time]

    def maximum(self) -> int:
        return -self.max_heap[0]

    def minimum(self) -> int:
        return self.min_heap[0]

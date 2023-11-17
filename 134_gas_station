"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        road_length = len(gas)
        short_trip_nets = [g-c for g,c in zip(gas, cost)]
        current_net = 0
        mini = 0
        mini_idx = -1
        for idx, a in enumerate(short_trip_nets):
            current_net += a
            if current_net<=mini:
                mini=current_net
                mini_idx = idx
        if current_net<0: return -1
        return (mini_idx+1)%road_length

        
        if road_length == 1: return (gas[0]>=cost[0])-1
        print(short_trip_nets)
        trip_length = 1
        trip_start = 0
        while short_trip_nets[trip_start] <0:
            trip_start+=1
            if trip_start == road_length: return -1
        while short_trip_nets[trip_start-1]>=0:
            trip_start = (trip_start-1)%road_length
        good_start = trip_start
        print(good_start)
        gas_totals = [short_trip_nets[good_start]]
        current_gas = gas_totals[0]
        while trip_length < road_length:
            if current_gas+short_trip_nets[(trip_start+trip_length)%road_length]>=0:
                print("c1", trip_start, trip_length, current_gas)
                current_gas+=short_trip_nets[(trip_start + trip_length)%road_length]
                if current_gas < min_gas[0]: min_gas = [current_gas, (trip_start + trip_length)%road_length]
                trip_length+=1
            else:
                print("c2", trip_start, trip_length, current_gas)
                while (current_gas < 0) or (current_gas + short_trip_nets[(trip_start + trip_length)%road_length] < 0):
                    current_gas = current_gas - short_trip_nets[trip_start] + short_trip_nets[(trip_start+trip_length)%road_length]
                    trip_start = (trip_start+1)%road_length
                    if trip_start == good_start: return -1
                
        return trip_start
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:53:46 2019

@author: arpit
"""

def findWaitingTime_fcfs(processes, n, 
                    bt, wt): 
  
    # waiting time for  
    # first process is 0 
    wt[0] = 0
  
    # calculating waiting time 
    for i in range(1, n ): 
        wt[i] = bt[i - 1] + wt[i - 1]  
  
# Function to calculate turn 
# around time 
def findTurnAroundTime_fcfs(processes, n,  
                       bt, wt, tat): 
  
    # calculating turnaround  
    # time by adding bt[i] + wt[i] 
    for i in range(n): 
        tat[i] = bt[i] + wt[i] 
  
# Function to calculate 
# average time 
def findavgTime_fcfs( processes, n, bt): 
  
    wt = [0] * n 
    tat = [0] * n  
    total_wt = 0
    total_tat = 0
  
    # Function to find waiting  
    # time of all processes 
    findWaitingTime_fcfs(processes, n, bt, wt) 
  
    # Function to find turn around  
    # time for all processes 
    findTurnAroundTime_fcfs(processes, n,  
                       bt, wt, tat) 
  
    # Display processes along 
    # with all details 
    #print( "Processes Burst time " + 
    #              " Waiting time " + 
     #           " Turn around time") 
  
    # Calculate total waiting time  
    # and total turn around time 
    for i in range(n): 
      
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(" " + str(i + 1) + "\t\t" + 
                    str(bt[i]) + "\t " + 
                    str(wt[i]) + "\t\t " + 
                    str(tat[i]))  
    #print( "Average waiting time = "+
                  #str(total_wt / n)) 
    #print("Average turn around time = "+
                   #  str(total_tat / n))
    return ((total_wt/n)+(total_tat/n))/2

  
# Driver code 
if __name__ =="__main__": 
      
    # process id's 
    processes = [ 1, 2, 3,4,5,6,7,8,9,10] 
    n = len(processes) 
  
    # Burst time of all processes 
    burst_time = [10,5,8,3,3,1,2,6,7,1]   
  
    findavgTime_fcfs(processes, n, burst_time) 
  
# This code is contributed  
# by ChitraNayal 
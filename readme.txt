#READING ASSIGNMENT AND PACKET ANALYSIS
Requirements:
Please install Scapy
pip3 install scapy

Note:
because of being constrainted by resources and computing power I couldn't run the complete file, Instead I took a small fragment of file to run the scripts. I believe scripts would run fine for complete file given enough system resources are available.
If needed one can add the file in the src folder and change filename in line 10 in PacketAnalysisDB/PacketAnalyser.py

Thank you.


******************************

TASK 1: 
aijax@aijax:~/Desktop/packet-Analysis-DB$ python3 task1.py 
ALL HTTP HEADERS 
 [{'Accept': b'*/*', 'Accept_Encoding': b'gzip, deflate', 'Accept_Language': b'en-US,en;q=0.5', 'Connection': b'keep-alive', 'Content_Length': b'83', '
Content_Type': b'application/ocsp-request', 'Host': b'status.rapidssl.com', 'User_Agent': b'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; 
...
...
..
..

***********************

TASK 2:
aijax@aijax:~/Desktop/packet-Analysis-DB$ python3 task2.py 

Enter 'p' to print the tuples in the table:

....
....
..

--    *     -----------------------    *    -----------------------    *   --------

(599, 63, 'ARP 172.16.7.68 > 172.16.7.1', "{('216.58.199.174', 443), ('172.16.80.219', 37916), ('13.35.202.115', 443), ('172.16.80.219', 45230)}", 'None', 'None')

---------------------    *     -----------------------    *    -----------------------    *   --------

(600, 56, 'ARP 172.16.7.64 > 172.16.7.1', "{('23.60.172.26', 80), ('172.16.80.219', 52324)}", 'None', 'None')

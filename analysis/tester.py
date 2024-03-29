#!/usr/bin/env python3

from tracer_common import TraceLine

count_wrong = 0

t1 = TraceLine('[Rank 91] MPI_Sendrecv started 1710421623.742759228, ended 1710421623.769690752 (elapsed 0.026931524), sending 4 bytes to dest 90, receiving 4 bytes')
if (not t1.source == 91) or \
   (not t1.bytes_sent == 4) or \
   (not t1.bytes_recv == 4) or \
   (not t1.bytes_total == 8) or \
   (not len(t1.recv_from) == 1) or \
   (not len(t1.sent_to) == 1):
    print("SendRecv validation failed!")
    count_wrong += 1

t2 = TraceLine('[Rank 91] MPI_Send started 1710421640.353019953, ended 1710421640.353580236 (elapsed 0.000560284), moved 4373184 bytes to receiver 89')
if (not t2.source == 91) or \
   (not t2.bytes_sent == 4373184) or \
   (not t2.bytes_recv == 0) or \
   (not t2.bytes_total == t2.bytes_sent) or \
   (not len(t2.recv_from) == 0) or \
   (not len(t2.sent_to) == 1):
    print(f"Send validation failed! t2.source={t2.source}, t2.bytes_sent={t2.bytes_sent}, t2.bytes_recv={t2.bytes_recv}, t2.bytes_total={t2.bytes_total}, len(t2.recv_from)={len(t2.recv_from)}, len(t2.sent_to)={len(t2.sent_to)}")
    count_wrong += 1

t3 = TraceLine('[Rank 91] MPI_Irecv started 1710421640.359012604, ended 1710421640.359500170 (elapsed 0.000487566), moved 4661928 bytes from source 95')
if (not t3.source == 91) or \
   (not t3.bytes_sent == 0) or \
   (not t3.bytes_recv == 4661928) or \
   (not t3.bytes_total == t3.bytes_recv) or \
   (not len(t3.recv_from) == 1) or \
   (not len(t3.sent_to) == 0):
    print(f"Receive validation failed! t3.source={t3.source}, t3.bytes_sent={t3.bytes_sent}, t3.bytes_recv={t3.bytes_recv}, t3.bytes_total={t3.bytes_total}, len(t3.recv_from)={len(t3.recv_from)}, len(t3.sent_to)={len(t3.sent_to)}")
    count_wrong += 1

t4 = TraceLine('[Rank 91] MPI_Allreduce started 1710421640.392734766, ended 1710421640.472914696 (elapsed 0.080179930), sent 4 bytes to MPI_COMM_WORLD')
if (not t4.source == 91) or \
   (not t4.bytes_sent == 4) or \
   (not t4.bytes_recv == 4) or \
   (not t4.bytes_total == t4.bytes_recv + t4.bytes_recv) or \
   (not len(t4.recv_from) == 1) or \
   (not len(t4.sent_to) == 1):
    print(f"Allreduce validation failed! t4.source={t4.source}, t4.bytes_sent={t4.bytes_sent}, t4.bytes_recv={t4.bytes_recv}, t4.bytes_total={t4.bytes_total}, len(t4.recv_from)={len(t4.recv_from)}, len(t4.sent_to)={len(t4.sent_to)}")
    count_wrong += 1

t5 = TraceLine('[Rank 94] MPI_Alltoall started 1711343528.706991673, ended 1711343528.707129717 (elapsed 0.000138044), sent 4 bytes to MPI_COMM_WORLD', nranks=384)
if (not t5.source == 94) or \
   (not t5.bytes_sent == (4 * 383)) or \
   (not t5.bytes_recv == (4 * 383)) or \
   (not t5.bytes_total == t5.bytes_recv + t5.bytes_recv) or \
   (not len(t5.recv_from) == 383) or \
   (not len(t5.sent_to) == 383):
    print(f"Alltoall validation failed! t5.source={t5.source}, t5.bytes_sent={t5.bytes_sent}, t5.bytes_recv={t5.bytes_recv}, t5.bytes_total={t5.bytes_total}, len(t5.recv_from)={len(t5.recv_from)}, len(t5.sent_to)={len(t5.sent_to)}")
    count_wrong += 1

t6 = TraceLine('[Rank 94] MPI_Alltoallv started 1711343528.709104776, ended 1711343528.709333181 (elapsed 0.000228405), sent 272 bytes total, max of 16 to rank 11 to MPI_COMM_WORLD')
if (not t6.source == 94) or \
   (not t6.bytes_sent == 272) or \
   (not t6.bytes_recv == 0) or \
   (not t6.bytes_total == t6.bytes_recv + t6.bytes_recv) or \
   (not len(t6.recv_from) == 0) or \
   (not len(t6.sent_to) == 0):
    print(f"Alltoallv validation failed! t6.source={t6.source}, t6.bytes_sent={t6.bytes_sent}, t6.bytes_recv={t6.bytes_recv}, t6.bytes_total={t6.bytes_total}, len(t6.recv_from)={len(t6.recv_from)}, len(t6.sent_to)={len(t6.sent_to)}")
    count_wrong += 1

if count_wrong == 0:
    print("Testing passed!")

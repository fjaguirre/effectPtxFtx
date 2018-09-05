from os import system as run
import time
'''
    LOST PACKETS:
    SNIR: Collisions, bit errors
        A packet was not received due to biterrors in header or payload. Collision due to
        interference.
    RxTx:
        A packet was not received because we were sending while receiving
'''
veinsDir = "/home/veins/src/veins/examples/veins/"
ftxArr = [x for x in range(1, 21)] # beacon rate array (from 1 per second to 20 per second)
ptxArr = [x for x in range(5, 41)] # txPower (from 5 mW to 40 mW)
simulation = 'cd /home/veins/src/veins/examples/veins && opp_run -r 0 -m -u Cmdenv -n .:../../src/veins --image-path=../../images -l ../../src/veins omnetpp.ini'
recvBeacons = []        
lostBeacons = []        
lostDueRxTx = []        
lostDueCollisions = []  
# strings to identify statics
recvKW = '].appl receivedBSMs '
lostKW = '].nic.mac1609_4 TotalLostPackets '
rxtxKW = '].nic.mac1609_4 RXTXLostPackets '
collKW = '].nic.phy80211p ncollisions '

# running simulations changing ftx and ptx
for f in ftxArr:
    for p in ptxArr:
        recv, lost, rxtx, coll = 0, 0, 0, 0
        cmd = 'python configScenario.py StaticBeaconing ' + str(f) + ' ' + str(p) + ' 2500 2500 200'
        run(cmd)
        run(simulation)
        time.sleep(5)
        # reading results
        results = open(veinsDir + 'results/General-#0.sca', 'r')
        lines = results.readlines()
        results.close()
        for line in lines:
            if recvKW in line:
                recv += int(line.split(recvKW)[1])
            elif lostKW in line:
                lost += int(line.split(lostKW)[1])
            elif rxtxKW in line:
                rxtx += int(line.split(rxtxKW)[1])
            elif collKW in line:
                coll += int(line.split(collKW)[1])
        recvBeacons.append(recv)
        lostBeacons.append(lost)
        lostDueRxTx.append(rxtx)
        lostDueCollisions.append(coll)
        print('\n[*] Ftx: ' + str(f) + '\tPtx: ' + str(p))
        print('     Collisions: ' + str(coll) + '\tTotal Losts: ' + str(lost) + '\tReceived: ' + str(recv))
        filex = open('resultados.txt', 'a')
        filex.write('\n[*] Ftx: ' + str(f) + '\tPtx: ' + str(p))
        filex.write('\n     Collisions: ' + str(coll) + '\tTotal Losts: ' + str(lost) + '\tReceived: ' + str(recv))
        filex.close()
        
print recvBeacons
print lostBeacons
print lostDueRxTx
print lostDueCollisions
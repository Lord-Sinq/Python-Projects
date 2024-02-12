def main():
    numHosts = 2
    thresholds = [64] * numHosts
    cwnd = [4] * numHosts
    channelCapacity = 64
    transmission_rates = [4] * numHosts
    iteration = 0
    while (iteration < 200):
        print("\nIteration " + str(iteration))

        if iteration == 25:
            for i in range(numHosts):
                cwnd[i] = 4
                transmission_rates[i] = 4
            thresholds.append(64)

        if iteration == 100:
            channelCapacity = 16

        if iteration == 130:
            channelCapacity = 128

        for i in range(len(cwnd)):
            transmission_rates[i] = cwnd[i]
        total_transmission_rate = sum(transmission_rates)

        for i in range(len(transmission_rates)):
            print("Host " + str(i) + ": " + format(transmission_rates[i], ".4f") + " (threshold = " + format(thresholds[i], "2d") + ")")

        print("Total transmission rate = " + format(total_transmission_rate, ".4f"))

        if total_transmission_rate > channelCapacity:
            for i in range(len(transmission_rates)):
                thresholds[i] = cwnd[i] // 2
                cwnd[i] = thresholds[i]
        else:
            for i in range(len(cwnd)):
                if cwnd[i] < thresholds[i]:
                    cwnd[i] *= 2
                else:
                    cwnd[i] += 1
        iteration += 1

if __name__ == "__main__":
    main()
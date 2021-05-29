# Find the average speed of vehicle, given the distance travelled for fixed time intervals

def compute_speed(lt,d):
    avg=sum(lt)/len(lt)
    return int(d/avg)
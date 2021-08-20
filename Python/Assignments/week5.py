class Tennis:
    def __init__(self, score):
        self.scores = score.split()
        self.stats = {}

    def init_empty_slot(self, player):
        self.stats[player] = {
            "bo5":0, 
            "bo3":0, 
            "sets_won":0, 
            "games_won":0,
            "sets_lost":0,
            "games_lost":0
            }

    def scan_sets(self, sets, p1, p2):
        """ Increments the sets won and lost
            based on their position in string. """
        (p1_points, p2_points) = sets.split("-")

        if p1_points > p2_points:
            self.stats[p1]["sets_won"] += 1
            self.stats[p2]["sets_lost"] += 1
        else:
            self.stats[p2]["sets_won"] += 1
            self.stats[p1]["sets_lost"] += 1

        # Games won by one player are games lost by another
        self.stats[p1]["games_won"] += int(p1_points)
        self.stats[p1]["games_lost"] += int(p2_points)

        self.stats[p2]["games_won"] += int(p2_points)
        self.stats[p2]["games_lost"] += int(p1_points)

    def is_bo5(self, li):
        """ Returns if the set is best of five
            or best of three. """
        scores = li.split(",")
        if len(scores) > 2:
            count = 0
            reached_two = False
            reached_three = False

            for s in scores:
                (p1, p2) = s.split("-")
                if p1 > p2:
                    count += 1
                    if count == 2:
                        reached_two = True
                    if count == 3:
                        reached_three = True
                        break
                else:
                    count = 0

            if reached_two:
                if reached_three or len(scores) > 3:
                    return True
                else:
                    return False
            else:
                if len(scores) == 3:
                    return False
                return True

        return False
 
    def fill_stats(self):
        for score in self.scores:
            temp = score.split(":")
            (p1, p2) = (temp[0], temp[1])
            
            if p1 not in self.stats:
                # Initialize an empty slot for each player
                self.init_empty_slot(p1)

            if p2 not in self.stats:
                self.init_empty_slot(p2) 

            if self.is_bo5(temp[2]):
                self.stats[p1]["bo5"] += 1
            else:
                self.stats[p1]["bo3"] += 1

            for sets in temp[2].split(","):
                # Increment the sets won, sets_lost
                # games_won, games_lost
                # based on player position
                self.scan_sets(sets, p1, p2)
                       
    def get_formatted_stats(self, lstats):
        """ Stores the necessary stats string in a list. """
        stats_list = []
        for stats in lstats:
            stat = "{0} {1} {2} {3} {4} {5} {6}".format(stats["player"],
                stats["bo5"],
                stats["bo3"],
                stats["sets_won"],
                stats["games_won"],
                stats["sets_lost"],
                stats["games_lost"])
            stats_list.append(stat)
        return stats_list

    def get_raw_stats(self):
        temp = []
        for player in self.stats:
            new_dict = self.stats[player]
            new_dict["player"] = player
            temp.append(new_dict)
        return temp

    def a_greater_than_b(self, a, b, criteria):
        return a[criteria] > b[criteria]

    def a_lesser_than_b(self, a, b, criteria):
        return a[criteria] < b[criteria]

    def a_equal_to_b(self, a, b, criteria):
        return a[criteria] == b[criteria]

    def print_list(self, li):
        for l in li:
            print(l)

    def get_stats_list(self):
        stats = self.get_raw_stats()
        #self.print_list(stats)
        stat_keys = list(stats[0].keys())
        stat_keys.remove('player')

        bigger = 0
        reverse_cat = ['sets_lost', 'games_lost'] 
        for j in range(0, len(stats)):
            for i in range(0, len(stats)):
                if i+1 >= len(stats):
                    break
                #print("\n\n",stats[i],"and \n",stats[i+1],"\n\n")
                if self.a_greater_than_b(a=stats[i+1], b=stats[i], criteria=stat_keys[0]):
                    #print("got in for {} and {}".format(stats[i+1], stats[i]))
                    stats[i], stats[i+1] = stats[i+1], stats[i]
                    break
                elif self.a_equal_to_b(a=stats[i+1], b=stats[i], criteria=stat_keys[0]):
                    #print("checkpoint #2")
                    for k in range(1, len(stat_keys)):
                        #print("checking {} for \n{}\n{}".format(stat_keys[k], stats[i+1], stats[i]))
                        if ((self.a_greater_than_b(a=stats[i+1], b=stats[i], criteria=stat_keys[k]) and 
                        stat_keys[k] not in reverse_cat) or
                        (stat_keys[k] in reverse_cat and
                        self.a_lesser_than_b(a=stats[i+1], b=stats[i], criteria=stat_keys[k]))):

                            #print("Swapping \n{}\nwith \n{} \nFOR {}".format(stats[i], stats[i+1], stat_keys[k]))
                            #print("\n\n")
                            stats[i], stats[i+1] = stats[i+1], stats[i]
                            break
                        elif self.a_greater_than_b(a=stats[i], b=stats[i+1], criteria=stat_keys[k]):
                            break
                            

        return stats
                    

if __name__ == "__main__":
    string = ""
    while True:
        current = input()
        if current == "":
            break
        else:
            string += ("\n"+current)

    tennis = Tennis(string)
    tennis.fill_stats()
    stats = tennis.get_stats_list()
    fstats = tennis.get_formatted_stats(stats)
    for s in fstats:
        print(s)


        

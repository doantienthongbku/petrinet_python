class Place:
    """
    Place of Petri Network
    """

    def __init__(self, holding):
        """
        holding is the number of token in the place
        """
        self.holding = holding


class ArcBase:
    """
    Base Arc of Petri Network
    """

    def __init__(self, place, amount=1):
        """
        place: the place acting as source/target of the arc in the network
        amount: The amount of token removed/added from/to the place
        """
        self.place = place
        self.amount = amount


class In(ArcBase):
    """
    In Arc of transition in Petri Network
    """

    def trigger(self):
        """
        Remove token
        """
        self.place.holding -= self.amount

    def non_blocking(self):
        """
        Validate action of outgoing arc is possible or not
        """
        return self.place.holding >= self.amount


class Out(ArcBase):
    """
    Out Arc of transition in Petri Network
    """

    def trigger(self):
        """
        Add token
        """
        self.place.holding += self.amount


class Transition:
    """
    Transition of Petri Network
    """

    def __init__(self, in_arcs, out_arcs):
        """
        in_arcs: Collection of ingoing arcs
        out_arcs: Collection of outgoing arcs
        """
        self.in_arcs = set(in_arcs)
        self.arcs = self.in_arcs.union(out_arcs)

    def fire(self):
        """
        Transition fire :v
        """
        not_blocked = all(arc.non_blocking() for arc in self.in_arcs)
        # Check the Transition is possible or not

        if not_blocked:
            for arc in self.arcs:
                arc.trigger()
        return not_blocked  # return if fired


class PetriNet:
    def __init__(self, transitions):
        """
        transitions: The transitions encoding the net
        """
        self.transitions = transitions

    def run(self, firing_sequence, ps):
        """
        firing_sequence: Sequence of transition names use for run
        ps: Place holdings to print during the run (debugging)
        """
        print("Using firing sequence:\n" + " => ".join(firing_sequence))
        print("Start {}\n".format([p.holding for p in ps]))

        for name in firing_sequence:
            t = self.transitions[name]
            if t.fire():
                print("{} fired!".format(name))
                print(" => {}".format([p.holding for p in ps]))
            else:
                print("{}...fizzled.".format(name))

        print("\nFinal {}".format([p.holding for p in ps]))

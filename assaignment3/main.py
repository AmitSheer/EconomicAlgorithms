import numpy

parties = ['אמת', 'ום', 'עם', 'ל', 'ג', 'ש"ס', 'כן', 'ט', 'פה', 'מחל']
votes = [175992.0, 178735.0, 194047.0, 213687.0, 280194.0, 392964.0, 432482.0, 516470.0, 847435.0, 1115336.0]
mandates = [4, 5, 5, 6, 7, 11, 12, 14, 24, 32]
total_votes = 4764742
total_mandates = 120


def f(s, divider):
    """
    basic formula
    :param s: amount of mandates
    :param divider: the influencing amount
    :return:
    """
    return s + divider


def calc(n_seats: [int], func, func_val):
    """
    find the party that has the highest value to get the mandate
    :param n_seats: num of mandates
    :param func:  the function to use for the calculation
    :param func_val: the value for the specific function
    :return:
    """
    curr_votes = []
    for i in range(len(parties)):
        curr_votes.append(votes[i] / func(n_seats[i], func_val))
    return numpy.argmax(curr_votes)


def get_mandates(func_val):
    new_mandates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(120):
        index = calc(new_mandates, f, func_val)
        new_mandates[index] = new_mandates[index] + 1
    return new_mandates


def webster():
    """
    implements the Webster Function
    :return:
    """
    new_mandates = get_mandates(0.5)
    printer(new_mandates)


def get_changes(new_mandates, old_mandates):
    """
    finds if there is any change between the old divide of the mandates to the new one
    :param new_mandates: mandate divide
    :param old_mandates: mandate divide
    :return:
    """
    benefited_parties = []
    at_loss_parties = []
    no_change_parties = []
    for i in range(len(parties)):
        if new_mandates[i] > old_mandates[i]:
            benefited_parties.append(parties[i])
        elif new_mandates[i] < old_mandates[i]:
            at_loss_parties.append(parties[i])
        else:
            no_change_parties.append(parties[i])
    return benefited_parties, at_loss_parties, no_change_parties


def printer(new_mandates):
    """
    prettify print of the results of the run
    :param new_mandates:
    :return:
    """
    # new_mandates = func()
    print(f'{new_mandates}')
    benefited_parties, at_loss_parties, no_change_parties = get_changes(new_mandates, mandates)
    print(f'benefited parties: {benefited_parties}')
    print(f'at loss parties: {at_loss_parties}')
    print(f'no change parties: {no_change_parties}')


def with_change():
    """
    finds the y for which the base mandate divide is changed
    :return:
    """
    flag = True
    y = 1
    # get base mandate without leftover law
    base_mandates = get_mandates(y)
    print(f'base mandates divided without leftover law: {base_mandates}')
    # run this loop until the divide changes and print the results of  the run
    while flag:
        man = get_mandates(y)
        bp, alp, ncp = get_changes(man, base_mandates)
        # check if the mandates
        if len(ncp) != 10:
            print(
                # the y for which the results changed
                f'max-min y for change   : {round(y, 3)}\n'
                # the new mandate spread
                f'this is the new mandate: {man}\n'
                # the correlating parties of the spread
                f'this is the parties    : {parties}')
            flag = False
        else:
            y = y + 0.001


if __name__ == '__main__':
    print('***************************** WEBSTER ******************************')
    webster()
    print('************************** Min-Max Change **************************')
    with_change()

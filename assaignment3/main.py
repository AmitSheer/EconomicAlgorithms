import numpy

parties = ['אמת', 'ום', 'עם', 'ל', 'ג', 'ש"ס', 'כן', 'ט', 'פה', 'מחל']
votes = [175992.0, 178735.0, 194047.0, 213687.0, 280194.0, 392964.0, 432482.0, 516470.0, 847435.0, 1115336.0]
mandates = [4, 5, 5, 6, 7, 11, 12, 14, 24, 32]
total_votes = 4764742
total_mandates = 120


def f(s, divider):
    return s + divider


def calc(n_seats: [int], func, func_val):
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
    new_mandates = get_mandates(0.5)
    printer(new_mandates)


def get_changes(new_mandates):
    benefited_parties = []
    at_loss_parties = []
    no_change_parties = []
    for i in range(len(parties)):
        if new_mandates[i] > mandates[i]:
            benefited_parties.append(parties[i])
        elif new_mandates[i] < mandates[i]:
            at_loss_parties.append(parties[i])
        else:
            no_change_parties.append(parties[i])
    return benefited_parties, at_loss_parties, no_change_parties


def printer(new_mandates):
    # new_mandates = func()
    print(f'{new_mandates}')
    benefited_parties, at_loss_parties, no_change_parties = get_changes(new_mandates)
    print(f'benefited parties: {benefited_parties}')
    print(f'at loss parties: {at_loss_parties}')
    print(f'no change parties: {no_change_parties}')


def with_change():
    flag = True
    y = 1
    while flag:
        man = get_mandates(y)
        bp, alp, ncp = get_changes(man)
        if ncp != 10:
            print(f'max-min y for change   : {y}\n'
                  f'this is the new mandate: {man}\n'
                  f'this is the parties    : {parties}')
            flag = False
        else:
            y = y + 0.001


if __name__ == '__main__':
    print('***************************** WEBSTER ******************************')
    webster()
    print('************************** Min-Max Change **************************')
    with_change()

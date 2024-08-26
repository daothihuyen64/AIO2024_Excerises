import numpy as np

# 4.1


def create_train_data():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)

# 4.2


def compute_prior_probablity(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))
    for i in range(len(y_unique)):
        prior_probability[i] = np.count_nonzero(
            train_data[:, 4] == y_unique[i]) / len(train_data)
    return prior_probability

# 4.3


def compute_conditional_probability(train_data):
    conditional_probability = []
    list_x_name = []
    count_no = np.count_nonzero(train_data[:, -1] == 'no')
    count_yes = np.count_nonzero(train_data[:, -1] == 'yes')
    for i in range(0, train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = []
        x_no = []
        x_yes = []
        for x in x_unique:
            x_id = np.nonzero((train_data[:, i] == x))[0]
            count_x_no = np.count_nonzero(train_data[x_id, -1] == 'no')
            count_x_yes = np.count_nonzero(train_data[x_id, -1] == 'yes')
            pro_x_no = count_x_no / count_no
            pro_x_yes = count_x_yes / count_yes
            x_no.append(pro_x_no)
            x_yes.append(pro_x_yes)
        x_conditional_probability.append(x_no)
        x_conditional_probability.append(x_yes)
        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name

# 4.4
def get_index_from_value(feature_name, list_features):
    return np.nonzero(list_features == feature_name)[0][0]

# 4.5
def train_naive_bayes( train_data ) :
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability , list_x_name = compute_conditional_probability ( train_data)
    return prior_probability , conditional_probability , list_x_name

# 4.6
def prediction_play_tennis (x , list_x_name , prior_probability , conditional_probability ):
    x1 = get_index_from_value ( x[0] , list_x_name [0])
    x2 = get_index_from_value ( x[1] , list_x_name [1])
    x3 = get_index_from_value ( x[2] , list_x_name [2])
    x4 = get_index_from_value ( x[3] , list_x_name [3])

    tmp = conditional_probability
    p0 = (tmp[0][0][x1]* tmp[1][0][x2]* tmp[2][0][x3]* tmp[3][0][x4]) * prior_probability[0]
    p1 = (tmp[0][1][x1]* tmp[1][1][x2]* tmp[2][1][x3]* tmp[3][1][x4]) * prior_probability[1]

    print(" no : ", p0)
    print(" yes : "  ,p1)
    if p0 > p1 :
        return 0
    return 1

    
#
train_data = create_train_data()
print(train_data)

# c14:
prior_probablity = compute_prior_probablity(train_data)
print("P( play tennis = No)", prior_probablity[0])
print("P( play tennis = Yes)", prior_probablity[1])

# c15:
conditional_probability, list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0], conditional_probability[0])
print("x2 = ", list_x_name[1], conditional_probability[1])
print("x3 = ", list_x_name[2], conditional_probability[2])
print("x4 = ", list_x_name[3], conditional_probability[3])


#c16:
outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook )
i2 = get_index_from_value("Rain", outlook )
i3 = get_index_from_value ("Sunny", outlook )
print ( i1 , i2 , i3 )


#c17 + c18:
x1 = get_index_from_value("Sunny", list_x_name[0])
print ("P( ' Outlook '= ' Sunny '| Play Tennis '= 'Yes ') = ", np.round(conditional_probability[0][1][x1], 2))
print ("P( ' Outlook '= ' Sunny '| Play Tennis '= 'No ') = ", np.round(conditional_probability[0][0][x1], 2))

#c19:
X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data ()
prior_probability , conditional_probability , list_x_name = train_naive_bayes ( data )
pred = prediction_play_tennis (X , list_x_name , prior_probability ,conditional_probability )
if( pred ) :
    print ("Ad should go!")
else :
    print ("Ad should not go!")
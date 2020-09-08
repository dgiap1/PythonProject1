life_expectancy_table = '''
=====Life Expectancy By Age and Gender (per 100,000)=====
Age:     Total:     Male:     Female:
0        100,000    100,000   100,000
1         99,422     99,370    99,477
5         99,326     99,261    99,393
10        99,268     99,199    99,341
15        99,191     99,107    99,280
20        98,937     99,749    99,134
25        98,466     98,071    98,983
30        97,872     97,235    98,543  
35        97,163     96,284    98,083
40        96,321     95,196    97,493
45        95,275     93,903    96,697
50        93,797     92,105    95,543
55        91,538     89,365    93,768
60        88,226     85,344    91,162
65        83,696     79,838    87,596
70        77,697     72,785    82,647
75        69,418     63,524    75,344
80        57,839     51,095    64,591
85        42,382     35,439    49,264
90        24,560     18,687    30,222
95         9,361      6,070    12,383
100        1,894        971     2,697

URL: https://www.cdc.gov/nchs/fastats/life-expectancy.htm
'''

life_expectancy_paired_tuple = (('Age: 0', 'Total: 100000', 'Male: 100000', 'Female: 100000'),
                                ('Age: 1', 'Total: 99422', 'Male: 99370', 'Female: 99477'),
                                ('Age: 5', 'Total: 99326', 'Male: 99261', 'Female: 99393'),
                                ('Age: 10', 'Total: 99268', 'Male: 99199', 'Female: 99341'),
                                ('Age: 15', 'Total: 99191', 'Male: 99107', 'Female: 99280'),
                                ('Age: 20', 'Total: 98937', 'Male: 99749', 'Female: 99134'),
                                ('Age: 25', 'Total: 99466', 'Male: 98071', 'Female: 98983'),
                                ('Age: 30', 'Total: 97872', 'Male: 97235', 'Female: 98543'),
                                ('Age: 35', 'Total: 97163', 'Male: 96284', 'Female: 98083'),
                                ('Age: 40', 'Total: 96321', 'Male: 95196', 'Female: 97493'),
                                ('Age: 45', 'Total: 95275', 'Male: 93903', 'Female: 96697'),
                                ('Age: 50', 'Total: 93797', 'Male: 92105', 'Female: 95543'),
                                ('Age: 55', 'Total: 91538', 'Male: 89365', 'Female: 93768'),
                                ('Age: 60', 'Total: 88226', 'Male: 85344', 'Female: 91162'),
                                ('Age: 65', 'Total: 83696', 'Male: 79838', 'Female: 97596'),
                                ('Age: 70', 'Total: 77697', 'Male: 72785', 'Female: 82647'),
                                ('Age: 75', 'Total: 69418', 'Male: 63524', 'Female: 75344'),
                                ('Age: 80', 'Total: 57839', 'Male: 51095', 'Female: 64591'),
                                ('Age: 85', 'Total: 42382', 'Male: 35439', 'Female: 49264'),
                                ('Age: 90', 'Total: 24560', 'Male: 18687', 'Female: 30222'),
                                ('Age: 95', 'Total: 9361', 'Male: 6070', 'Female: 12383'),
                                ('Age: 100', 'Total: 1894', 'Male: 971', 'Female: 2697'))

class Expectancy:
    def __init__(self, age, total, male, female):
        self.age = age
        self.total = total
        self.male = male
        self.female = female
        
pop_zero = Expectancy(0, 100000, 100000, 100000)
pop_one = Expectancy(1, 99422, 99370, 99477)
pop_five = Expectancy(5, 99326, 99261, 99393)
pop_ten = Expectancy(10, 99268, 99199, 99341)
pop_fifteen = Expectancy(15, 99191, 99107, 99280)
pop_twenty = Expectancy(20, 98937, 99749, 99134)
pop_twenty_five = Expectancy(25, 98466, 98071, 98983)
pop_thirty = Expectancy(30, 97872, 97235, 98543)
pop_thirty_five = Expectancy(35, 97163, 96284, 98083)
pop_forty = Expectancy(40, 96321, 95196, 97493)
pop_forty_five = Expectancy(45, 95275, 93903, 96697)
pop_fifty = Expectancy(50, 93797, 92105, 95543)
pop_fifty_five = Expectancy(55, 91538, 89365, 93768)
pop_sixty = Expectancy(60, 88226, 85344, 91162)
pop_sixty_five = Expectancy(65, 83696, 79838, 87596)
pop_seventy = Expectancy(70, 77697, 72785, 82647)
pop_seventy_five = Expectancy(75, 69418, 63524, 75344)
pop_eighty = Expectancy(80, 57839, 51095, 64591)
pop_eighty_five = Expectancy(85, 42382, 35439, 49264)
pop_ninety = Expectancy(90, 24560, 18687, 30222)
pop_ninety_five = Expectancy(95, 9361, 6070, 12383)
pop_hundred = Expectancy(100, 1894, 971, 2697)



# Q1.Write a program to print the number that end with 7 in the given list.

def print_numbers_ending_with_7(numbers):
  for i in numbers:
    if i % 10 == 7:
      print(i)
numbers = [135,2,45,24,57,6,765,45,13,65,7,68,98,9764322,47687,87,98,9,98] 
print_numbers_ending_with_7(numbers)
# # output :  57,7,47687,87 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Q2.

 
# The function takes a single parameter, operations, which is expected to be a list of strings representing various file operations 
def find_unique_operations(operations):
    # Inside the function, an empty dictionary named folders is initialized. This dictionary will store folder names as keys and corresponding sets of operations as values.
    folders = {}  


    # The function iterates through the list of operations using a for loop.
    for operation in operations:
        parts = operation.split(' ', 1)
        # The length of parts is checked. If it's not equal to 2, which would indicate an invalid operation format, the loop proceeds to the next iteration using continue.
        if len(parts) != 2:
            continue
        action, folder = parts
        # If the action is "goto", the current_folder is updated to the value of the folder. This keeps track of the current folder being operated upon.
        if action == "goto":
            current_folder = folder
        else:

            # if the current_folder is already present in the folders dictionary. If not, a new set is created for the current_folder and added to the folders dictionary.
            if current_folder not in folders:
                folders[current_folder] = set()    
                # print("folders----------------" , folders)        
            folders[current_folder].add(action)
    # print("Totalfolder----------------------------", folders.items())
    for folder, operations in folders.items():
        # print("songle_folder------------------------------" , operations )
        if len(operations) > 0:
            print("operationsn______", operations)
            if len(operations) == len(set(operations)):
                # print("folder->>>>>>>>>>>>>>>>>>>>>>>>>>>" , folder)
                return folder

    return None

# Sample inputs
sample_input_1 = [
"goto folderA","create fileA","create fileB","create fileA",
 "goto folderB",
"goto folderC","create fileA","create fileB","create fileC"
] 


sample_input_2 = [
"goto folderA", "create fileB","create fileB",
"create fileA", "create fileB", "goto folderB",
"goto folderC", "create fileA", "create fileB","create fileB"
] 


sample_input_3 = [
"goto folderA", 
"goto folderB",
"goto folderC","create fileA","create fileB","create fileC"
]


# Calculate and print the outputs
output_1 = find_unique_operations(sample_input_1)
output_2 = find_unique_operations(sample_input_2)
output_3 = find_unique_operations(sample_input_3)

print("Sample Output 1:", output_1)  # FolderA
print("Sample Output 2:", output_2)   #folderA
print("Sample Output 3:", output_3)     #folderC



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Q3

def generate_fibonacci_series(n):
    # The initial three terms [0, 1, 1] are hardcoded in the fibonacci_series list to serve as the base for generating subsequent terms.
    fibonacci_series = [0, 1, 1]
    # Inside the while loop, the code calculates the next term in the series by summing the last three terms of the fibonacci_series list.
    while len(fibonacci_series) < n:
        # The sum of these three terms gives the next term in the series.
        sum_next_num = fibonacci_series[-1] + fibonacci_series[-2] + fibonacci_series[-3]
        fibonacci_series.append(sum_next_num)
        # The function returns the fibonacci_series list, which now contains the generated series of Fibonacci-like terms.
    return fibonacci_series

num_terms = 50
fibonacci_series = generate_fibonacci_series(num_terms)

print("Fibonacci sequence:")
for num in fibonacci_series:
    print(num)




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Q4.
# class User(models.Model):
# 	name = models.CharField(max_length=30)
# 	email = models.CharField(max_length=30)

# class Item(models.Model):
# 	name = models.CharField(max_length=100)
# 	sku_code = models.CharField(max_length=20, unique=True)
# 	price = models.FloatField()
# 	create_timestamp = models.DateTimeField()
# 	created_by = models.ForeignKey(User)

# class Order(models.Model):
# 	date = models.DateField()
# 	item = models.ForeignKey(Item)
# 	quantity = models.IntegerField()
# 	ordered_by = models.ForeignKey(User)

#Q1. List the Orders with quantity more than 10

    # Orders_with_quantity_gt_10 = Order.objects.filter(quantity__gt=10)

#Q2 List the Orders which are having “Samsung” in their Item’s name...

    # samsung_orders = Orders.objects.filter(item__name__icontains = "Samsung")


#Q3 Print the total sum of the quantity of all orders of the item_id 23

    # total_quantity_item_23 = Order.object.filter(item__id = 23).(total_quantity=models.Sum('quantity'))
    # print(total_quantity_item_23['total_quantity'])




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>










# Q5. Print all the numbers from the given input string.

def find_number(data):
  for i in data :
    if i.isdigit():
        print(i)
data = "ijoYitvFDXrewst#Y$65u6&GyHJghfcjtey4w532a^$S85(*&ohinyuiy futdyrw6e 4e8t yuvftcrde7r%*^7gituvcYRey"
find_number(data) 

# // OUTPUT: 6,5,6,4 ,5,3,2,8,5,6,4,8,7,7




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Q6.Print the following output in stdout.

def triangle(n):
    for i in range(n):
        print("")
        for j in range(i+1):
            print("*",end="")
triangle(6)
''' OUTPUT:- 
#   *
#   **
#   ***
#   ****
#   *****
#   ******
'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#Q7.Print the sum of 4th Column in the above dataframe

def sum_of_column(data):
    sum_of_data = 0
    col_number = 4
    for i in data :
        sum_of_data = sum_of_data + i[col_number-1]
    print(sum_of_data)
data = [ 
[10, 20, 4, 66, 56, 6, 12],
[1, 60, 64, 6, 5, 556, 612],
[176, 623, 6545, 126, 521, 55, 62]
]
sum_of_column(data)
 #OUTPUT : 198



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Q8
import json
import matplotlib.pyplot as plt

# The function takes a list of records as input, where each record represents a student's name and their assessment scores.
def create_graph(records):
    students = []
    exam_scores = []
    quiz_scores = []
    homework_scores = []
    try:
        for record in records:
            students.append(record["name"])
            for score_data in record["scores"]:
                if score_data["type"] == "exam":
                    exam_scores.append(score_data["score"])
                elif score_data["type"] == "quiz":
                    quiz_scores.append(score_data["score"])
                elif score_data["type"] == "homework":
                    homework_scores.append(score_data["score"])
    except Exception as e :
        print(e)

    # The plt.figure function is used to create a new figure with a specific size.
    plt.figure(figsize=(10, 6)) 
    #Three plt.bar calls are used to create the bars for exams, quizzes, and homework scores. The bottom parameter is used to stack the bars on top of each other.
    plt.bar(students, exam_scores, label="Exam")
    plt.bar(students, quiz_scores, bottom=exam_scores, label="Quiz")
    plt.bar(students, homework_scores, bottom=[sum(x) for x in zip(exam_scores, quiz_scores)], label="Homework")
    # This function sets the label for the x-axis of the chart.
    # In this case, the label is set to "Students," indicating that the x-axis represents different students.
    plt.xlabel("Students")
    # This function sets the label for the y-axis of the chart
    # The label "Scores" indicates that the y-axis represents the assessment scores of the students.
    plt.ylabel("Scores")
    # This function sets the label for the y-axis of the chart
    plt.title("Student Assessment Scores")
    #  ->  plt.legend() adds a legend to the chart.
    plt.legend()
    # -> plt.xticks(rotation=45) rotates the x-axis labels for better visibility.
    plt.xticks(rotation=45)
    # ->plt.tight_layout() ensures that all elements fit properly in the figure, and plt.show() displays the chart.
    plt.tight_layout()
    plt.show()

# This line opens the file named "students.json" in read mode ("r").
with open("students.json", "r") as file:
    # This line reads the content of the opened file and assigns it to the variable data.
    data = file.read()
# This line uses the json.loads() function to parse the JSON-formatted string (data) 
records = json.loads(data)
#  here i call the function with give arguments records   
create_graph(records)



























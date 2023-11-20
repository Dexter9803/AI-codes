
marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))


print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
    ele = float(input())
    marks.append(ele)  # adding the element

print("The marks of",n,"students are : ")
print(marks)


def Selection_Sort(marks):

    for i in range(len(marks)):

        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(marks)):
            if marks[min_idx] > marks[j]:
                min_idx = j

        # Swap the minimum element with the first element
        marks[i], marks[min_idx] = marks[min_idx], marks[i]

    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(marks)):
        print(marks[i])
Selection_Sort(marks)
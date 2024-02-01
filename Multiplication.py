# print multiplication table for a number between the range 0-10.
# create a repository on github to push it there. 
# create a dockerfile(with the prerequisites to run the code) and place in github.
# run a pipeline with the repository on github that'll create an image eventually.

for i in range(0,11):
    print("\n \t")
    for j in range(0,11):
        print(f"{i*j}\t", end="\t")
import os
import csv

# Set path for file
csvpath = os.path.join("..","Resources","election_data.csv")
file_to_output = os.path.join("..","Output", "Output.txt")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

total_votes = 0
candidates = []
candidates_votes = []

for row in csvreader:
        #skip 1st row
        if row[0]=="Voter ID":
            next
        else:
            totalvotes+=1
            if row[2] not in candidates:
                candidates.append(row[2])
                candidates_votes.append(1)
            if row[2] in candidates:
                candidates_votes[candidates.index(row[2])]=candidates_votes[candidates.index(row[2])]+1

#calculate the winning candidate and non-winning candidates
maxm=str(candidates[candidates_votes.index(max(candidates_votes))])
print("Results")
print("------------------")           
print("Total Votes: "+str(total_votes))
print("------------------")

for i in range(len(candidates)):
        print(candidates[i]+": "+"{0:.3%}".format((candidates_votes[i]-1)/total_votes)+" ("+str(candidates_votes[i]-1)+")")
    print("-------------------------")
    print("Winner: "+maxm)
    print("-------------------------")
    
with open(file_to_output, "w") as txt_file:
    txt_file.write("Results"+"\n")
    txt_file.write("-----------------"+"\n")           
    txt_file.write("Total Votes: "+str(total_votes)+"\n")
    txt_file.write("-----------------"+"\n")
    
    #printing the candidates with all of their vote counts and percentages
    for i in range(len(candidates)):
        txt_file.write(candidates[i]+": "+"{0:.3%}".format((candidates_votes[i]-1)/total_votes)+" ("+str(candidates_votes[i]-1)+")"+"\n")
    txt_file.write("-------------------------"+"\n")
    txt_file.write("Winner: "+maxm+"\n")
    txt_file.write("-------------------------"+"\n")
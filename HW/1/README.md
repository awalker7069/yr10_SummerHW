#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
We use binary because at the basic level computers only use on and off switches.
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
In binary code, it would be represented as 10010011.
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
b5 = 181
```
###4 - Here is a function written is **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
**users** is part of an if statement, the data type is a boolean.
```

(b) What type of data is returned by this function? **(1 mark)**
```
The type of data returned is a boolean.
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
line 7, OUTPT should be spelt as OUTPUT.
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
A syntax error is when the program cannot run because of small mistakes such as spelling errors or things not being definined.
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
???
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
???
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
???
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe: Bus Topology is a network of computers where they are all connected to a single device/ cable.

Advantages: Easy to set-up, costs a very little amount of money.

Disadvantages: Limit to the cable length required, requires terminators to dump signals, it is difficult to detect troubleshooting on a single computer, not suitable for heavily used networks.
```

**Ring Topology (6 marks)**
```
Describe: A Ring Topology is, hence the name, a network in which all the computers are connected to eachother in a ring/ circular shape. 

Advantages: Very organised network set-up, additional devices/ components do not effect the overall set-up and capablity of the network.

Disadvantages: If one computer workstation goes down the whole network is affected, network is highly dependent on the wire connecting the workstations together.
```

**Star Topology (6 marks)**
```
Describe: Star Topology is a network where all the computers/ workstations are connected up to a central hub system that runs the whole network.

Advantages: Has a high perform similar to the Bus Topology, relatively easy to connect new nodes to the network.

Disadvantages: Has too much dependence on the central to keep the network constantly up and running, overall cost to run the network is not cheap.
``` 

# CODING INTERVIEW UNIVERSITY NOTES
## Big O Notation
https://www.youtube.com/watch?v=iOq5kSKqeR4

- O(n) >> the time required to count characters in a string is linear
- len = 1000 (stored number of elements) >> asymptotically constant operation, O(1) >> we already know how many characters
- binary search runs in O(logN) >> array of size 8 runs in 3 operations (log(base2)8), size 16 in log(base2)16 or 4 operations
	+ OMEGA is the best case scenario, in the case of binary search, OMEGA would be if the first middle termwas the term we were looking for
	+ given an array size 3, [1,2,3], if our wanted term is 1 then our program runs in OMEGA(1); if our wanted term is 3, then our program runs in OMEGA(N) (where N represented the length of the array)
- THETA >> best and worst cases are the same

## Quick Tutorial Video
https://www.youtube.com/watch?v=V6mKVRU1evU

- A way to measure how well a computer algorithm scales as the amount of data involved increases.
- 0(1) >> order of one - no matter how the inputs scale, the growth will be the same ***check
- "N" >> the amount of data
- 0(N) >> order of N - the time taken to process grows linearly with the values used
	+ LINEAR SEARCH FOR VALUE
- O(N^2) -> order of N squared - the time taken to process is the size of N squared
	+ BUBBLE SORT
- 0(log n) >> 
	+ BINARY SEARCH
- O(n log n) >> 

...


## Omega and Theta
https://www.youtube.com/watch?v=ei-A_wy5Yxw

- Mathematical Description -
	- f(n) is O(g(n)) if C and n(sub 0)
	f(n) <= Cg(n) for all n>n(sub 0)
	- O(g(n)) vs 'OMEGA'(g(n)) vs 'THETA'

	- 'THETA' => f(n) is 'THETA'(g(n)) if
		1. f(n) is O(g(n))
		2. f(n) is 'OMEGA'(g(n))

- What it all means in the realm of computer science?
	- our time function can show us the dominating term, the part of the equation that requires the most processing power
		+ 4n^2 + 16n + 2 >>> the 4n^2 term will occupy most of the processing as n increases
	- log(base10)(1000) = 3 >>> how many times do you multiply 10 to get 1000? 3
	- log(basex)(n) => O(log(basex)(n)

...


## Asymptotic Notation
https://www.youtube.com/watch?v=gSyDMtdPNpU

- the knapsack problem >> given a problem, a solution may work sometimes and not others and a broken solution may work in different cases
- the RAM Model of Computation
	+ each "simple" operation (+,-,=,if,call) takes 1 step
	+ loops and subroutine calls are not simple operations. they depend on the size of the data and the contents of a subroutine. "Sort" is not a single step operation
	+ each memory acces takes exactly 1 step
	+ we measure the run time of an algorithm by counting the number of steps, where: this model is useful and accurate in the same sense as the flat-earth model (which is useful)
- Worst-Case Complexity >> the function of an algorithm defined by the maximum number of steps taken on any instance of size n >> the most useful case of complexity vs average case and best case
- its easier to talk about upper and lower bounds of the function >> Asumptotic notation or Big O notation (O,Theta,Omega)
- g(n) = O(f(n)) means C x f(n) is an upper bound on g(n)
- g(n) = OMEGA(f(n)) means C x f(n) is a lower bound g(n)
...
- a function multiplied by a constant doesnt change its asymptotics


## Asymptotic Analysis
https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98

- asymptotic analysis - the study of how algorithms behave as the size of the data grows very large or to infinity

### Big Oh Notation is used to represent upper bounds of a function
- let n be the size of programs INPUT
- let T(n) be a function e.g. running time
- let f(n) be another function, preferable simple
- T(n) is in O(f(n)) if and only if T(n) <= Cf(n) >> need a constant, C that will make T(n) less than Cf(n)
- FORMALLY >> O(f(n)) is the set of all functions T(n) that satisfy:
	+ there exist postive constants C and N such that, for all n >= N, T(n) <= cf(n)
	+ N is the place where the vertical line is drawn for the proof
	+ Big O notation doesn't care about (most) constant factors >> unnecessary to write O(2n)
- Big O notation is usually used to indicate dominating (fastest-growing) term
### Table of Important Big O Sets
- smallest to largest >>
----------------------------------------
	FUNCTION   |   COMMON NAME

	O(1)       |   constant
	CO(logn)   |   
	CO
...
- O(nlogn) or faster time: considered "efficient"
- n^7 or slower time: considered useless
- ***need to understand logarithms >> study them if you dont***
- WARNINGS:
	1. fallacious proof >> c must be a constant (can't involve n)
	2. Big O notation does not say what the functions are >> indicates a relationship between the functions	
	3. ...
	4. Big O notation doesn't always tell the whole story

## Amortized Analysis
https://www.youtube.com/watch?v=B3SpQZaAZP4

- opening a duncan donuts >> franchise cost $1,000,000 and cost per donut $1
	+ should the first donut cost $1,000,001? NO. the cost needs to be spread out
	+ assume we will sell 1m donuts, we can sell each donut for $2 each, if we wanted to make a $1 profit we'd need to sell them for $3 a piece
	+ taking a big amount of money and scattering it over time
- Binary Counter - 0000 to 0001 requires 1 unit of working >> 0001 to 0010 is 2 units of work
	+ k = 4 bits >> O(nk)?
	+ every even increment of the binary counter is 1
	+ we always bring some number of people home and send one guy up with a roundtrip ticket (see binary counter example about cost to increment)

## Computational Complexity
https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/

- questions to answer before starting to code: 
	+ is my algorithm worth implementing?
	+ will it solve the largest test cases in time?
	+ if there are other solutions, which should i choose?
- check the number of records and determine if multiple algorithms should be used >> if it is small enough, run algorithm 1, otherwise run algorithm2
- usually we are looking for the behaviour of the program in the worst possible case >> what is the worst input with 700 elements? >> how fast does the maximum runtime grow when we increase the input size?
- an algorithm with runtime proportional to N^2 will always be better than an algorithm with runtime proportional to N^3 on almost all inputs
- f(N) is O(g(N)), if for some c almost the entire graph of the function f is below the graph of the function >> this means that f grows at most as fast as c.g does
- f(N) E O(g(N)) >> we do not use "=" to explain this relationship literally as they are not equal, therefore we can us "E" to denote their relationship
- ^^ defined above is Big O notation and is used to specify upper bounds on function growth
## Arrays
### Arrays (Basic Data Structures)
https://www.coursera.org/lecture/data-structures/arrays-OsBSF

- contiguous area of memory consisting of equal-size elements indexed by contiguous integers
- constant time acces to read/write any point in an array >> array_addr + elem_size x (i - first_index)
--------------------
TIMES FOR COMMON OPERATIONS
                | ADD   REMOVE
Beginning       | O(n)  O(n)
End             | O(1)  O(1)
Middle          | O(n)  O(n)

### Linear and Multi-Dim Arrays
https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE

- **LECTURE MOSTLY REFERENCING JAVA**
- simplest form of LOOP is "while" loop

public static boolean is Prime(int n) {
        int divisor = 2;
        while(divisor < n){
                if (n % divisor == 0){
                        return false;
                }
                divisor++;
        }
        return true;
}
  - object consisting of a numbered list of variables. Eace is a primitive type or reference
  - in Java - different data types can be stored in arrays if OBJECT type array is used, cannot be done using primitive data types (char, int...)
  - in Java - string is considered an OBJECT data type
  - field "c.length" - length of array >> cannot redefine length with c.length = 7; //compile-time ERROR
  - multi-dimensional arrays >> an array of references to arrays
  - PASCAL'S TRIANGLE

## Linked Lists
https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0

- linked list >> made up of 'nodes'
	- nodes >> an item
		>> a reference to next node in the list
(JAVA)
public class ListNode {
	int item;
	ListNode next;
}
l1 = new ListNode(), l2 = new ListNode(), l3 = new ListNode();
l1.item = 7;
l2.item = 0;
l3.item = 6;

l1.next = l2;
l2.next = l3;
l3.next = null;
- can only refer to an object, not a variable (java)
- NODE OPERATIONS
	- public ListNode(int item, ListNode next){
		this.item = item;
		this.next = next;
	}
	public ListNode(int item){
		this(item, null)
	}
- advantages over array lists:
	- inserting item into middle of linked list takes constant time IF you have reference to previous node
	- list can keep growing until memore runs out
- inserts a new item after 'this':
	public void insertAfter(int item){
		next = new ListNode(item,next);
	}
	>> "from some other method", call l2.insertAfter(3);
- disadvantages:
	- finding the nth item of a linked list takes time proportional to n >> constant-time array lists is an advantage

(finding the nth item in a list:

	public ListNode nth(int position){
		if (position == 1){
			return this;
		} else if ((position < 1) || (next == null)){
			return null;
		} else{
			return next.nth(position - 1);
		}
	}
- LISTS OF OBJECTS
	- reference any object by declaring reference of type Object (java)
- A List Class
	- 2 problems with SListNodes
		1. x and y pointing to same list >> insert a new item at beginning of list >> x = new SListNode("soap", x); >> x will point to new node but y will point to old node
		2. how do you represent an empty list? >> if x = null; run-time error if you call a method on a null object,
	- SOLUTION: separate SList class maintains head of list

## Linked Lists II
https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w

- a PRIVATE method or field is invisible & inaccessible to other classes
	- reasons:
		1. to prevent data from being corrupted by other classes
		2. you can improve the implementation without causing other classes to fail
	"there is an advantage gained from declaring all of your vulnerable parts private" XD
								- Instructor Jonathan Shewchuk
- interface of a class: prototypes for public methods, plus descriptions of their behaviors
- Abstract Data Type(ADT): a class with a well-defined interface, but implementation details are firmly hidden from other classes
- Invariant: a fact about a data structure that is always true
	- "A Date object always represents a valid date."
- not all classes are ADTs! Some classes are just data storage units (no invariants).
### The SList ADT
- another advantage of SList class:
	- SList ADT enforces 2 invariants:
		1. 'size' is always correct
		2. list is never circularly linked
	- both goals accomplished because only SList methods can change the lists
- SList ensures this:
	1. the fields of SList (head and size) are 'private'
	2. no method of SList returns an SList Node.
### Doubly-Linked Lists
- inserting/deleting at front of list is easy
- inserting/deleting at end of list takes a long time

class DListNode{              |          class DList{
	Object item;          |          	private DListNode head;
	DListNode next;       |          	private DListNode tail;
	DListNode prev;       |          }
}

- insert & delete items at both ends in constant running time
	- removes the tail node (at least 2 items in DList):
		tail.prev.next = null;
		tail = tail.prev;
- sentinel >> a special node that does not represent an item
	- DList v.2: circularly linked

class DListNode{              |          class DList{
	Object item;          |          	private DListNode head;
	DListNode next;       |          	private int size;
	DListNode prev;       |          }
}
- DList invariants with sentinel:
	1. For any DList d, d.head != null
	2. For any DlistNode x, x.next != null
	3. For any DListNode x, x.prev != null
	4. For any DListNode x, if x.next == y, then
	   For any DListNode x, x.prev == x
	5. For any DListNode x, if x.prev == y, then y.next == x
	6. A DList's "size" variable is # of DListNodes NOT COUNTING SENTINEL	
	-Empty Dlist: sentinel's prev & next field point to itself
	
## C Code
https://www.youtube.com/watch?v=QN6FPiD0Gzo

#include<stdio.h>
#include <conio.h>
#include<stdlib.h>
struct node
{
	int data;
	struct node *next;
};
struct node *head;	//head pointer holds the address of the starting node of the linked list;
int createlinkedlist()
{
	struct node *newmnode,*temp;
	newnode = (struct node*)malloc(sizeof(struct node)); //creation of a newnode
	printf("\n\n\t Enter the data into the linkedlist:- ");
	scanf("%d",&newnode->data);
	newnode->next=NULL;
	if(head == NULL)
	{
		head = newnode;
		return 1;
	}
	else
	{
		temp = head;
		while(temp->next!=NULL)
		{
			temp = temp->next;

		}
		temp->next = newnode;
	}
}
void display()
{
	node *temp;
	temp = head;
	if(head!=NULL)
	{
		for(temp = head;temp!=NULL;temp = temp->next)
		{
			printf("%d\t",temp->data);
		}
	}
	else
	{
		printf("\n\n\t The list is empty....,");
	}
}
int main()
{
	int ch;
	head = NULL;		//tell that the list is empty
	do
	{
	printf("\n\n\t 1.create linkedlist");
	printf("\n\n\t 2.Display linkedlist");
	printf("\n\n\t 3.exit");
	printf("\n\n\t Enter our choice:- ");
	scanf("%d",&ch);
	switch(ch)
	{
	case 1:
		createlinkedlist();
		break;
	case 2:
		display();
		break;
	case 3:
		exit(1);
		break;
	default:
		printf("\n\n\t Wrong entry try again....,");
		break;
	}
	}while(ch!=3);
}

## Core Linked Lists vs Arrays
https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9

- it takes O(n) to add an element to the front of an ArrayList >> all elements have to shift
- ArrayList fails in efficiency for fulfilling this task
- Linked List is a better option
- Singly Linked List nodes only point to next node >> Doubly Linked List nodes point to prev and next
- Sentinel (dummy) nodes >> dont store data, exist even when list is empty, live at beginning and end of list, head/tail pointer points to these, not needed but useful
- O(n) to access an arbitrary location of element within the linked list

## Real World Linked Lists vs Arrays
https://www.coursera.org/lecture/data-structures-optimizing-performance/in-the-real-world-lists-vs-arrays-QUaUd

- reading an array is constant time
- have to walk down a list to get to an element O(n)
- using a list to do a merge sort of lots of data was a "big win"

## Why You Should Avoid Linked Lists
https://www.youtube.com/watch?v=YQs6IC-vgmo

- using linked lists uses more random accesses vs vectors
- linked lists have multiple points of data, the data and the 2 pointers, the vectors are more simple and although it has to shift all the data, caches are efficient at managing such operations
### Vector v List
- the amount of memory used differ dramatically
	- list uses 4+ words per element
		- it will be worse for 64-bit architectures
		- 100,000 list elements take up 6.4MB or more (but I have Gigabytes!?)
	- vector uses 1 word per element
		- 100,000 list elements take up 1.6MB or more
- memory access is relatively slow
	- caches, pipelines, etc.
	- 200 to 500 instructions per memory access
	- unpredictable memory access gives many more cache misses
- implications:
	- don't store data unnecessarily
	- keep data compact
	- access memory in a predictable manner

## Doubly-Linked Lists
https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD

- popback O(1)
- constant time to insert at or remove from the front
- with tail and doubly-linked, constant time to insert at or remove from the back
- O(n) time to find arbitrary element
- list elements need not be contiguous
- with doubly-linked list, constant time to insert between nodes or remove a node

## Stacks
https://www.coursera.org/lecture/data-structures/stacks-UdKzQ

- think of the operations can be done with a stack of books
- push an opening paren/bracket onto the stack and check if the next in line will be closing, if not then you dont have a balanced set of parens/brackets
- Push(x) >> appending O(1)
- Top() >> the top element will be the same as n elements >> a, b, two elements b will be the top
- Pop() >> pulls off the top >> a, b, pop(b) leaves only a
- for a linked list >> pop becomes popFront, top is topFront >> HEAD, d, c, b, a
- stacks can be implemented with either an array or a linked list
- each stack operation is O(1): Push, Pop, Top, Empty
- stacks are occassionaly known as LIFO queus (Last In First Out)

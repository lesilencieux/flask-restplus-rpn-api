# A Reverse Polish Notation calculator


## You have two options to test this code

# FIRST OPTION  : Run directly ``rpn.py`` in in ``core/rpn.py``

Please follow the steps for this first option 

## Usage

clone the repository

Simply run `rpn.py`. You can push numbers as you'd do in a RPN calculator, and stack them with operators.

The following example will calculate `((5 + 7) * 3) / (9 + 3)`:

```
$ python3 rpn.py
> 3 7 5 + *
stack: [36.0]
36.0
> 9 3
stack: [27.0 9.0 3.0]
> + /
stack: [2.25]
3.0
```

### Quick operation

If you're in a hurry and just need to calculate a small / simple expression, you can pass this expression as an argument in the command-line, like this:

```
$ python3 rpn.py 642 47 + 15 /
stack: [45.93333333333333]
45.93333333333333
```

**IMPORTANT**: if your expression uses the '\*' operator (multiplication), you'll **have** to surround your expression by a single quote. All of this because '\*' would be interpreted as "the list of the files in the current directory".

Example:

```
$ rpn.py 642 47 '*' 15 /
stack: [2011.6]
2011.6
$ rpn.py '642 47 * 15 /'
stack: [2011.6]
2011.6
```

## Available functions / operators

Type `help` to display the list of the available operators.

* classic operators: `+`, `-`, `*`, `/`,
* modulo, using either: `mod` or `%` (e.g.: `5 2 mod` => `1.0`)
* power, using either: `^`, `**`, `pwr` (e.g.: `3 4 **` => `81.0`)
* square root: `sqrt` (e.g.: `144 sqrt` => `12`)
* natural logarithm: `ln` (e.g.: `81 ln` => `4.39444915467`)
* n-based logarithm: `log` (e.g.: `42 3 log` => `3.4021735027328797`)
* absolute value: `abs` (e.g.: `-4.33 abs` => `4.33`)
* round up and down: `ceil` & `floor` (e.g: `1.54 ceil 1.54 floor` => `[2.0 1.0]`)
* well-known constants: `pi` & `e`
* simple trigonometry: `sin`, `cos` & `tan`.

Stack-related functions

* `clear`: clears the stack,
* `drop`: removes the element at the top of the stack,
* `dup`: duplicates the element at the top of the stack,
* `swap`: take the two topmost elements and swap them,

# FIRST OPTION  : Run it as API and test via swagger-ui

 clone the repository

 You can start this API in your OS using virtual environnemnt (recommended) but it is better to 
 start it in docker container  

 All you need to start it in docker container is granted executing permission to `deploy.sh` and execute it 

```
 Grant permission 

 $ chmod +x deploy.sh

 Deployment 

 $ ./deploy.sh

 ```
 Wait until deployment to finish

 If it success you must be able to see the swagger-ui like this otherwise check if do not have an other 
 container started on port 5001

 Go to this url http://localhost:5001

 Illustrate image : https://github.com/lesilencieux/flask-restplus-rpn-api/blob/main/assets/1.png

 So let's start test it 

 1 ===>> For the fist time we got  "The stack is empty." it is normal because we do not add anything 

  Illustrate image : https://github.com/lesilencieux/flask-restplus-rpn-api/blob/main/assets/2.png

  so we are going to push somes number
 2 ====>>

  I push 1O and 20 to stack like this :

  {
   "total": "10"
  }

 Illustrate image : https://github.com/lesilencieux/flask-restplus-rpn-api/blob/main/assets/3.png

 If we try again to read the stack we must see :

 "[10.0, 20.0]"

 Illustrate image : https://github.com/lesilencieux/flask-restplus-rpn-api/blob/main/assets/4.png

 Time to clean stack
  3 ====>>

  We have this 

  Illustrate image : https://github.com/lesilencieux/flask-restplus-rpn-api/blob/main/assets/5.png”

   If we try to read the stack again we will see  "The stack is empty."

   Now time to test the operations 

   ## Available functions / operators

Type `help` to display the list of the available operators.

* classic operators: `+`, `-`, `*`, `/`,
* modulo, using either: `mod` or `%` (e.g.: `5 2 mod` => `1.0`)
* power, using either: `^`, `**`, `pwr` (e.g.: `3 4 **` => `81.0`)
* square root: `sqrt` (e.g.: `144 sqrt` => `12`)
* natural logarithm: `ln` (e.g.: `81 ln` => `4.39444915467`)
* n-based logarithm: `log` (e.g.: `42 3 log` => `3.4021735027328797`)
* absolute value: `abs` (e.g.: `-4.33 abs` => `4.33`)
* round up and down: `ceil` & `floor` (e.g: `1.54 ceil 1.54 floor` => `[2.0 1.0]`)
* well-known constants: `pi` & `e`
* simple trigonometry: `sin`, `cos` & `tan`.

Stack-related functions

* `clear`: clears the stack,
* `drop`: removes the element at the top of the stack,
* `dup`: duplicates the element at the top of the stack,
* `swap`: take the two topmost elements and swap them,

For the Available operators you have just to pass your argument in this json format using correct order 
according your operation 

input :
{
  "total": "3 7 5 + *"
}
Illustrate image : https://github.com/lesilencieux/flask-restplus-rpn-api/blob/main/assets/6.png”
result :

{
  "total": "36.0"
}
 Illustrate image : https://github.com/lesilencieux/flask-restplus-rpn-api/blob/main/assets/7.png



# If the images I use to illustrate does not appear correctly you can show it directly in /assets folder
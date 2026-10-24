# Terminal Record: Ridgeline Tool Rental

## 1. Building the project
Yusra% mkdir -p ism3232-midterm

Yusra% cd ism3232-midterm

Yusra% git init
Initialized empty Git repository in /home/yusra/ism3232-midterm/.git/

Yusra% git branch -M main

Yusra% git remote add origin https://github.com/YusraBatool50/ism3232-midterm.git

Yusra% pwd
/home/yusra/ism3232-midterm

Yusra% touch business_rules.py main.py commands.md README.md requirements.txt .gitignore tests/
touch: cannot touch 'tests/': No such file or directory

Yusra% ls -a
.     .gitignore         commands.md

..    README.md          main.py

.git  business_rules.py  requirements.txt

Yusra% mkdir tests

Yusra% touch tests/__init__.py tests/test_business_rules.py

Yusra% tree -a -I '.git'
.

├── .gitignore

├── README.md

├── business_rules.py

├── commands.md

├── main.py

├── requirements.txt

└── tests

    ├── __init__.py

    └── test_business_rules.py



2 directories, 8 files

Yusra% python3 -m venv .venv
Yusra% source .venv/bin/activate

(.venv) Yusra% pip install pytest ruff
Successfully installed iniconfig-2.3.1 packaging-26.3 pluggy-1.7.0 pygments-2.21.0 pytest-9.1.1 ruff-0.17.2

(.venv) Yusra% pip freeze > requirements.txt

(.venv) Yusra% cat requirements.txt
iniconfig==2.3.1

packaging==26.3

pluggy==1.7.0

Pygments==2.21.0

pytest==9.1.1

ruff==0.17.2

(.venv) Yusra% echo '.venv/' > .gitignore

(.venv) Yusra% echo '__pycache__/' >> .gitignore

(.venv) Yusra% cat .gitignore
.venv/

__pycache__/

(.venv) Yusra% code business_rules.py

(.venv) Yusra% code main.py

(.venv) Yusra% git add business_rules.py main.py

(.venv) Yusra% git commit -m "For the first part of the midterm, I began by setting up the structure of my ism3232-midterm folder. My next steps were to build the logic for business_rules.py and main.py, which is when I wrote down my eight functions while taking the appropriate constraints, aka the business rules regarding teh discounts, into account. My final step for this portion of the project was to paste the list into main.py, and import my function. I had to modify the code a bunch of times to achieve the output. Initially, I forgot to account for the business rules which gave me the wrong output, so I rewrote my code to reflect that and finally got the right output."
[main (root-commit) 187ef21] For the first part of the midterm, I began by setting up the structure of my ism3232-midterm folder. My next steps were to build the logic for business_rules.py and main.py, which is when I wrote down my eight functions while taking the appropriate constraints, aka the business rules regarding teh discounts, into account. My final step for this portion of the project was to paste the list into main.py, and import my function. I had to modify the code a bunch of times to achieve the output. Initially, I forgot to account for the business rules which gave me the wrong output, so I rewrote my code to reflect that and finally got the right output.
 2 files changed, 157 insertions(+)
 create mode 100644 business_rules.py
 create mode 100644 main.py

 (.venv) Yusra% git push origin main
 Enumerating objects: 4, done.

Counting objects: 100% (4/4), done.

Delta compression using up to 8 threads

Compressing objects: 100% (4/4), done.

Writing objects: 100% (4/4), 1.82 KiB | 311.00 KiB/s, done.

Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

To https://github.com/YusraBatool50/ism3232-midterm.git

 * [new branch]      main -> main

 (.venv) Yusra% git add -A

 (.venv) Yusra% git commit -m "Added all the project files, hadn't pushed all of them and didn't realize"
 [main 22f3986] Added all the project files, hadn't pushed all of them and didn't realize

 6 files changed, 8 insertions(+)

 create mode 100644 .gitignore

 create mode 100644 README.md

 create mode 100644 commands.md

 create mode 100644 requirements.txt

 create mode 100644 tests/__init__.py

 create mode 100644 tests/test_business_rules.py

 (.venv) Yusra% git push -u origin main
 Enumerating objects: 7, done.

Counting objects: 100% (7/7), done.

Delta compression using up to 8 threads

Compressing objects: 100% (4/4), done.

Writing objects: 100% (6/6), 665 bytes | 166.00 KiB/s, done.

Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

To https://github.com/YusraBatool50/ism3232-midterm.git

   187ef21..22f3986  main -> main

branch 'main' set up to track 'origin/main'.

(.venv) Yusra% code tests/test_business_rules.py

(.venv) Yusra% git commit -m "At this point in the assignment, I have began writing my 20 pytests. For documentation purposes, I will write an explanation for some of these pytests to communicate the logic I used to build the code. The first test returns the applicable rental discount rate using a conditional statement. If the number of days is greater than or equal to 7, then a 20 percent discount is applied. If the number of days is lesser than or equal to 3, then the standard discount of 10 percent is applied. Otherwise, the discount is zero. Finally, we account for the contractor discount as well, using AND. If there is a licensed contractor, they will automatically qualify for a 10 percent discount as specified in the business rules."

(.venv) Yusra% git push -u origin main
Enumerating objects: 5, done.

Counting objects: 100% (5/5), done.

Delta compression using up to 8 threads

Compressing objects: 100% (3/3), done.

Writing objects: 100% (3/3), 686 bytes | 343.00 KiB/s, done.

Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)

remote: Resolving deltas: 100% (2/2), completed with 2 local objects.

To https://github.com/YusraBatool50/ism3232-midterm.git

   22f3986..4a5a5ce  main -> main

branch 'main' set up to track 'origin/main'.

Yusra% git commit --allow-empty -m "Correcting an error from my previous comment. I was under the impression that the testbusinessrulespy file was for writing functions but this was an error on my part. I put the appropriate code into businessrulespy, where we are actually calling the functions. At this stage I am still a little confused as to what these tests are meant to do but I will go through lab 7 and try to figure it out"
[main 0d15646] Correcting an error from my previous comment. I was under the impression that the testbusinessrulespy file was for writing functions but this was an error on my part. I put the appropriate code into businessrulespy, where we are actually calling the functions. At this stage I am still a little confused as to what these tests are meant to do but I will go through lab 7 and try to figure it out

Yusra% git push origin main
Enumerating objects: 1, done.

Counting objects: 100% (1/1), done.

Writing objects: 100% (1/1), 397 bytes | 397.00 KiB/s, done.

Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

To https://github.com/YusraBatool50/ism3232-midterm.git

   4a5a5ce..0d15646  main -> main

(.venv) Yusra% pytest -v
\============ test session starts ============
platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.7.0 -- /home/yusra/ism3232-midterm/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/yusra/ism3232-midterm
collected 22 items
tests/test_business_rules.py::test_calculate_rental_cost_over_multiple_days PASSED [  4%]
tests/test_business_rules.py::test_get_rental_discount_before_three_days PASSED [  9%]
tests/test_business_rules.py::test_get_rental_discount_at_three_days PASSED [ 13%]
tests/test_business_rules.py::test_get_rental_discount_before_seven_days PASSED [ 18%]
tests/test_business_rules.py::test_get_rental_discount_at_seven_days PASSED [ 22%]
tests/test_business_rules.py::test_get_rental_discount_contractor PASSED [ 27%]
tests/test_business_rules.py::test_requires_deposit_below_limit PASSED [ 31%]
tests/test_business_rules.py::test_requires_deposit_at_limit FAILED [ 36%]
tests/test_business_rules.py::test_needs_inspection_below_five_days PASSED [ 40%]
tests/test_business_rules.py::test_needs_inspection_at_five_days PASSED [ 45%]
tests/test_business_rules.py::test_needs_inspection_at_quote_limit FAILED [ 50%]
tests/test_business_rules.py::test_needs_inspection_above_quote_limit PASSED [ 54%]
tests/test_business_rules.py::test_total_quoted_two_rentals PASSED [ 59%]
tests/test_business_rules.py::test_total_quoted_empty_list PASSED [ 63%]
tests/test_business_rules.py::test_format_rental_line_no_requirements PASSED [ 68%]
tests/test_business_rules.py::test_format_rental_line_both_requirements PASSED [ 72%]
tests/test_business_rules.py::test_largest_rental_two_customers PASSED [ 77%]
tests/test_business_rules.py::test_largest_rental_tie PASSED [ 81%]
tests/test_business_rules.py::test_largest_rental_empty_list PASSED [ 86%]
tests/test_business_rules.py::test_calculate_quote_below_waiver_limit PASSED [ 90%]
tests/test_business_rules.py::test_calculate_quote_at_waiver_limit FAILED [ 95%]
tests/test_business_rules.py::test_calculate_quote_with_discount PASSED [100%]
\================= FAILURES ==================
______ test_requires_deposit_at_limit _______
    def test_requires_deposit_at_limit():
>       assert requires_deposit(1000.00) is True
E       assert False is True
E        +  where False = requires_deposit(1000.0)
tests/test_business_rules.py:45: AssertionError
___ test_needs_inspection_at_quote_limit ____
    def test_needs_inspection_at_quote_limit():
>       assert needs_inspection(5, 800.00) is False
E       assert True is False
E        +  where True = needs_inspection(5, 800.0)
tests/test_business_rules.py:57: AssertionError
___ test_calculate_quote_at_waiver_limit ____
    def test_calculate_quote_at_waiver_limit():
>       assert round(calculate_quote(150.00, 1), 2) == 150.00
E       assert 175.0 == 150.0
E        +  where 175.0 = round(175.0, 2)
E        +    where 175.0 = calculate_quote(150.0, 1)
tests/test_business_rules.py:113: AssertionError
\========== short test summary info ==========
FAILED tests/test_business_rules.py::test_requires_deposit_at_limit - assert False is True
FAILED tests/test_business_rules.py::test_needs_inspection_at_quote_limit - assert True is False
FAILED tests/test_business_rules.py::test_calculate_quote_at_waiver_limit - assert 175.0 == 150.0
\======= 3 failed, 19 passed in 0.29s ========

(.venv) Yusra% python -m pytest -v --cache-clear
\============ test session starts ============
platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.7.0 -- /home/yusra/ism3232-midterm/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/yusra/ism3232-midterm
collected 22 items
tests/test_business_rules.py::test_calculate_rental_cost_over_multiple_days PASSED [  4%]
tests/test_business_rules.py::test_get_rental_discount_before_three_days PASSED [  9%]
tests/test_business_rules.py::test_get_rental_discount_at_three_days PASSED [ 13%]
tests/test_business_rules.py::test_get_rental_discount_before_seven_days PASSED [ 18%]
tests/test_business_rules.py::test_get_rental_discount_at_seven_days PASSED [ 22%]
tests/test_business_rules.py::test_get_rental_discount_contractor PASSED [ 27%]
tests/test_business_rules.py::test_requires_deposit_below_limit PASSED [ 31%]
tests/test_business_rules.py::test_requires_deposit_at_limit PASSED [ 36%]
tests/test_business_rules.py::test_needs_inspection_below_five_days PASSED [ 40%]
tests/test_business_rules.py::test_needs_inspection_at_five_days PASSED [ 45%]
tests/test_business_rules.py::test_needs_inspection_at_quote_limit PASSED [ 50%]
tests/test_business_rules.py::test_needs_inspection_above_quote_limit PASSED [ 54%]
tests/test_business_rules.py::test_total_quoted_two_rentals PASSED [ 59%]
tests/test_business_rules.py::test_total_quoted_empty_list PASSED [ 63%]
tests/test_business_rules.py::test_format_rental_line_no_requirements PASSED [ 68%]
tests/test_business_rules.py::test_format_rental_line_both_requirements PASSED [ 72%]
tests/test_business_rules.py::test_largest_rental_two_customers PASSED [ 77%]
tests/test_business_rules.py::test_largest_rental_tie PASSED [ 81%]
tests/test_business_rules.py::test_largest_rental_empty_list PASSED [ 86%]
tests/test_business_rules.py::test_calculate_quote_below_waiver_limit PASSED [ 90%]
tests/test_business_rules.py::test_calculate_quote_at_waiver_limit PASSED [ 95%]
tests/test_business_rules.py::test_calculate_quote_with_discount PASSED [100%]
\============ 22 passed in 0.12s =============

(.venv) Yusra% python main.py
Ridgeline Tool Rental - Rental Report

Alvarez: $145.00 | deposit: no | inspection: no

Brennan: $133.00 | deposit: no | inspection: no

Chowdhury: $306.00 | deposit: no | inspection: no

Dvorak: $960.00 | deposit: no | inspection: yes

Eastman: $1344.00 | deposit: yes | inspection: yes

Fujita: $900.00 | deposit: no | inspection: no

Garza: $427.50 | deposit: no | inspection: no

Hughes: $1120.00 | deposit: yes | inspection: yes

Rentals: 8

Total quoted: $5335.50

Average quote: $666.94

Largest quote: Eastman

Deposits required: 2

Inspections required: 3

(.venv) Yusra% git commit -m "I was running into some of my tests failing so I cleared pytest's cache. I did refer to the internet but not AI for this task because I tried everything I could and checked my business rules three times but nothing seemed out of place or inaccurate. The only command I looked up was that of clearing pytest's cache and it worked and all 22 of my tests passed so that is how I resolved that issue"
[main a5ba93e] I was running into some of my tests failing so I cleared pytest's cache. I did refer to the internet but not AI for this task because I tried everything I could and checked my business rules three times but nothing seemed out of place or inaccurate. The only command I looked up was that of clearing pytest's cache and it worked and all 22 of my tests passed so that is how I resolved that issue
 2 files changed, 130 insertions(+), 12 deletions(-)

 (.venv) Yusra% git push origin main
 Enumerating objects: 8, done.

Counting objects: 100% (8/8), done.

Delta compression using up to 8 threads

Compressing objects: 100% (5/5), done.

Writing objects: 100% (5/5), 1.63 KiB | 557.00 KiB/s, done.

Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)

remote: Resolving deltas: 100% (2/2), completed with 2 local objects.

To https://github.com/YusraBatool50/ism3232-midterm.git

   0d15646..a5ba93e  main -> main

(.venv) Yusra% ruff check .
I001 [*] Import block is un-sorted or un-formatted
  --> main.py:4:1

I001 [*] Import block is un-sorted or un-formatted
  --> tests/test_business_rules.py:4:1

Found 2 errors.
[*] 2 fixable with `--fix`.

(.venv) Yusra% ruff check . --fix
Found 2 errors (2 fixed, 0 remaining).

(.venv) Yusra% ruff check .
All checks passed!

(.venv) Yusra% pytest -v
\============ test session starts ============
platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.7.0 -- /home/yusra/ism3232-midterm/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /home/yusra/ism3232-midterm
collected 22 items
tests/test_business_rules.py::test_calculate_rental_cost_over_multiple_days PASSED [  4%]
tests/test_business_rules.py::test_get_rental_discount_before_three_days PASSED [  9%]
tests/test_business_rules.py::test_get_rental_discount_at_three_days PASSED [ 13%]
tests/test_business_rules.py::test_get_rental_discount_before_seven_days PASSED [ 18%]
tests/test_business_rules.py::test_get_rental_discount_at_seven_days PASSED [ 22%]
tests/test_business_rules.py::test_get_rental_discount_contractor PASSED [ 27%]
tests/test_business_rules.py::test_requires_deposit_below_limit PASSED [ 31%]
tests/test_business_rules.py::test_requires_deposit_at_limit PASSED [ 36%]
tests/test_business_rules.py::test_needs_inspection_below_five_days PASSED [ 40%]
tests/test_business_rules.py::test_needs_inspection_at_five_days PASSED [ 45%]
tests/test_business_rules.py::test_needs_inspection_at_quote_limit PASSED [ 50%]
tests/test_business_rules.py::test_needs_inspection_above_quote_limit PASSED [ 54%]
tests/test_business_rules.py::test_total_quoted_two_rentals PASSED [ 59%]
tests/test_business_rules.py::test_total_quoted_empty_list PASSED [ 63%]
tests/test_business_rules.py::test_format_rental_line_no_requirements PASSED [ 68%]
tests/test_business_rules.py::test_format_rental_line_both_requirements PASSED [ 72%]
tests/test_business_rules.py::test_largest_rental_two_customers PASSED [ 77%]
tests/test_business_rules.py::test_largest_rental_tie PASSED [ 81%]
tests/test_business_rules.py::test_largest_rental_empty_list PASSED [ 86%]
tests/test_business_rules.py::test_calculate_quote_below_waiver_limit PASSED [ 90%]
tests/test_business_rules.py::test_calculate_quote_at_waiver_limit PASSED [ 95%]
tests/test_business_rules.py::test_calculate_quote_with_discount PASSED [100%]
\============ 22 passed in 0.15s =============

(.venv) Yusra% git add business_rules.py main.py tests/test_business_rules.py

(.venv) Yusra% git commit -m "Completed business rule functions and verified 22 pytest tests"
[main 984e98a] Completed business rule functions and verified 22 pytest tests

 2 files changed, 8 insertions(+), 7 deletions(-)

 (.venv) Yusra% git push origin main
 Enumerating objects: 9, done.

Counting objects: 100% (9/9), done.

Delta compression using up to 8 threads

Compressing objects: 100% (5/5), done.

Writing objects: 100% (5/5), 590 bytes | 295.00 KiB/s, done.

Total 5 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)

remote: Resolving deltas: 100% (3/3), completed with 3 local objects.

To https://github.com/YusraBatool50/ism3232-midterm.git

   a5ba93e..984e98a  main -> main

(.venv) Yusra% code commands.md
(.venv) Yusra%

## 2. The virtual environment
(.venv) Yusra% which python3
/home/yusra/ism3232-midterm/.venv/bin/python3

The .venv/bin/python3 shows that the virtual environment is active.

## 3. The project structure
(.venv) Yusra% tree -L 2
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
(.venv) Yusra%

The .venv folder is on my computer but not in my GitHub repository because it is in .gitignore. 

## 4. Every function and test
(.venv) Yusra% rg 'def '
business_rules.py
17:def calculate_rental_cost(daily_rate: float, days: int) -> float:
21:def get_rental_discount(days: int, contractor: bool = False) -> float:
35:def calculate_quote(
47:def requires_deposit(quote: float) -> bool:
50:def needs_inspection(days: int, quote: float) -> bool:
57:def total_quoted(rentals: list) -> float:
70:def largest_rental(rentals: list) -> str:
88:def format_rental_line(

tests/test_business_rules.py
17:def test_calculate_rental_cost_over_multiple_days():
21:def test_get_rental_discount_before_three_days():
25:def test_get_rental_discount_at_three_days():
29:def test_get_rental_discount_before_seven_days():
33:def test_get_rental_discount_at_seven_days():
37:def test_get_rental_discount_contractor():
41:def test_requires_deposit_below_limit():
45:def test_requires_deposit_at_limit():
49:def test_needs_inspection_below_five_days():
53:def test_needs_inspection_at_five_days():
57:def test_needs_inspection_at_quote_limit():
61:def test_needs_inspection_above_quote_limit():
65:def test_total_quoted_two_rentals():
73:def test_total_quoted_empty_list():
78:def test_format_rental_line_no_requirements():
83:def test_format_rental_line_both_requirements():
89:def test_largest_rental_two_customers():
97:def test_largest_rental_tie():
105:def test_largest_rental_empty_list():
109:def test_calculate_quote_below_waiver_limit():
113:def test_calculate_quote_at_waiver_limit():
117:def test_calculate_quote_with_discount():
(.venv) Yusra%

Business_rules.py defines 8 functions. Tests/test_business_rules.py contains 22 tests.

## 5. Which files print
(.venv) Yusra% rg -l 'print'
main.py

Main.py contains print statements because it displays the Ridgeline Tool Rental Report. 

## 6. The commit history
(.venv) Yusra%  git log --oneline
984e98a (HEAD -> main, origin/main) Completed business rule functions and verified 22 pytest tests
a5ba93e I was running into some of my tests failing so I cleared pytest's cache. I did refer to the internet but not AI for this task because I tried everything I could and checked my business rules three times but nothing seemed out of place or inaccurate. The only command I looked up was that of clearing pytest's cache and it worked and all 22 of my tests passed so that is how I resolved that issue
0d15646 Correcting an error from my previous comment. I was under the impression that the testbusinessrulespy file was for writing functions but this was an error on my part. I put the appropriate code into businessrulespy, where we are actually calling the functions. At this stage I am still a little confused as to what these tests are meant to do but I will go through lab 7 and try to figure it out
4a5a5ce At this point in the assignment, I have began writing my 20 pytests. For documentation purposes, I will write an explanation for some of these pytests to communicate the logic I used to build the code. The first test returns the applicable rental discount rate using a conditional statement. If the number of days is greater than or equal to 7, then a :

I had made 7 commits by this point. 
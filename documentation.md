## CODE DOCUMENTATION: WEB SCRAPING
### BY: Mercy Nyamusi
### PROBLEM SOLVING APPROACH
#### LIBRARIES USED
> <strong>requests</strong><br/>
> To enable the fetching of inforation from the website using the <strong>.get()</strong> method<br/>
> <strong>beautifulsoup4<em>(bs4)</em></strong><br/>
> To enable parsing through the <em>requests.get()</em> result so as to get information specified in the <strong>.select()</strong> and <strong>.find()</strong> methods.
###### LOGIC
> <strong>Step1</strong>: Retrieve information from the website using <strong>requests</strong> library.<br/>
> <strong>Step2</strong>: Use <strong>bs4</strong> library to identify the <em>main tags</em> containing information on all the books on the website page.<br/>
> <strong>Step3</strong>: From the result in step 2 identify the <em>HTML tags</em> and <em>their attributes</em> which contain the <em>book titles</em>, <em>number of reviews</em> and the <em>price</em> information.<br/>
> <strong>Step4</strong>: Iterate through the result from <strong>Step2</strong>, while singling out components within the tags identified in <strong>step3</strong> i.e assign components with the <em>book titles</em> in a book title variable, <em>reviews</em> in a book review variable and <em>price</em> in a book price variable.<br/>
> <strong>Step5</strong>: Store the information: title, reviews and price in a dictionary where <strong>book</strong> is the <strong>key</strong> and a <strong>list containing the price and reviews</strong> is the <strong>value</strong>.  <br/>
> <strong>Step6</strong>: Retrieve the book <strong>reviews</strong> from the dictionary, store them in a list and <strong>sort</strong> the list in <strong>descending</strong> order.<br/>
> <strong>Step7</strong>: Select the <strong>top 30</strong> books with most reviews and match them to their book titles.<br/>
> <strong>Step8</strong>: Create a new dictionary with the top 30 books with the most reviews.<br/>
> <strong>Step9</strong>: Retrieve the book <strong>prices</strong> from the dictionary, store them in a list and <strong>sort</strong> the list in <strong>descending</strong> order.<br/>
> <strong>Step10</strong>:Select the <strong>top 10 </strong>books with <strong>highest prices</strong> and match them to their book titles.<br/>
> <strong>Step11</strong>:Create a new dictionary with the top 30 books with the most reviews.<br/>
> <strong>Step12</strong>:Print the key and values of the dictionary from <strong>step11</strong> which contains the <em>top 10 most expensive books from the top 30 most popular ones</em>.


###### FUNCTIONS USED
><strong>book_info()</strong><br/>
> Function to fetch book information: title, number of reviews and price.<br/>
> <strong>review()</strong><br/>
> Function to filter the top 30 books with most reviews.<br/>
> <strong>price()</strong><br/>
> Function to filter the top 10 most expensive books from the 30 books with most reviews.<br/>
> <strong>display()</strong><br/>
> Function to display information on the top 10 most expensive books among the top 30 with most reviews.

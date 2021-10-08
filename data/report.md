# Data Engineering Bootcamp

### Miguel Angel Rodriguez Sayeg


1. **How many commercial chains are monitored, and therefore, included in this database?** 706.
2. **What are the top 10 monitored products by State?** 

3. **Which is the commercial chain with the highest number of monitored products?** WAL-MART with 8643133.
4. **Use the data to find an interesting fact.**
5. **What are the lessons learned from this exercise?**   
I learned that working with a higher-level NoSQL framework requires a certain way of thinking that should not be internally mixed with the way of writing raw SQL clauses.  
Also, it was really important to check beforehand if there are any potential mistakes with the data you are working with before assuming there are not any. For instance, in the dataset there was a mistake with the way a float64 was stored in the 'precio' tag, and it was necessary to decide the best strategy of ignoring the field without affecting the analysis for other items.
7. **Can you identify other ways to approach this problem? Explain.** Yes, using other kind of technologies such as Apache Spark or Hadoop to iterate to the data in a faster way with the pre-existing tools. However, in this case I decided to use pandas and Python because of its simplicity and because, by using chunks of data, the data processing stage was not as slow as I initially expected.

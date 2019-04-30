# Tennis WTA

Small project example treating historical data of the Women Tennis Association (WTA) based on data curated by Jeff Sackmann. For further information:

- Source: https://github.com/JeffSackmann/tennis_wta
- Examples: https://github.com/JeffSackmann/tennis_atp/tree/master/examples

## Code

- **Sports - Tennis**: Jupyter Notebook with all the steps to work with data related to the WTA and perform some ETL processes (extract data from source files, load into NoSQL database, transform data), data analysis and visualizations (using matplotlib, geopandas and plotly).


## Setup
To properly run the code in the Jupyter Notebook, you should first set up your environment and the project structure.
- Install MongoDB (server and client, like MongoDB Compass): https://docs.mongodb.com/manual/installation/
- Start mongo server. Command for Unix-based OS:
          
          ```shell
          
          $ sudo service mongod start
          ```
- Create the database and the empty collections names as follows:
  - Database: **tennis_wta**
    - Collections:
      - **wta_players**
      - **wta_matches**
      - **wta_rankings**


- Download the project or clone the repository:

          ```shell
          
          $ git clone https://github.com/routarddev/data-science
          $ cd data_science/tennis_wta/
          ```
  Verify that the files folder contains the CSV files.
  
  You can also download them from the curator's original project: https://github.com/JeffSackmann/tennis_wta          

- Install the required packages in the current environment, if working with Anaconda, or in the system otherwise:

          ```shell

          $ pip install pymongo
          $ pip install jupyter
          $ pip install pandas
          $ pip install matplotlib
          $ pip install seaborn
          $ pip install descartes
          $ pip install geopandas
          $ pip install mapclassify
          $ pip install plotly
          ```

- Finally, run jupyter notebook within the project folder

          ```shell
          
          $ jupyter notebook
          ```
  Alternative, use this command to open the url manually in your browser (including the token):

          ```shell
          
          $ jupyter notebook --no-browser
          [I 11:51:02.843 NotebookApp] Serving notebooks from local directory: /.../tennis_wta
          [I 11:51:02.843 NotebookApp] The Jupyter Notebook is running at:
          [I 11:51:02.843 NotebookApp] http://localhost:8888/?token=f592e3a9f94783dd85068edd65fd6a3246369e287df41a88
          [I 11:51:02.844 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
          [C 11:51:02.849 NotebookApp] 
          ```
  

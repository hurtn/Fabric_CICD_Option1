# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "98fa3eaf-cc3a-4c12-b5c2-3ac8cc194a76",
# META       "default_lakehouse_name": "Lakehouse",
# META       "default_lakehouse_workspace_id": "93da8d9d-198a-43c4-bf90-54839045807c",
# META       "known_lakehouses": [
# META         {
# META           "id": "98fa3eaf-cc3a-4c12-b5c2-3ac8cc194a76"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

df = spark.sql("SELECT * FROM Lakehouse.publicholidays LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

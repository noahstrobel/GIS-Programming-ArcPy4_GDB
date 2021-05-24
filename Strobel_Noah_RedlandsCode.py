# Name: Noah Strobel

# Class: GISc-450

# Created: 04/07/2021

# Purpose: This program asks users to enter the directory name
# for the "Redlands.gdb" geodatabase. Users have 3 chances to enter the correct
# name before the program terminates and must be re-run.
# If the correct GDB information is entered, the program prints out the GDB's contents
# to the console and writes the same output to a .txt file.
# The information examined and printed include: GDB name; GDB directory; and the number of
# feature datasets contained within the GDB. Finally, it prints feature class names, types,
# and number of records.


import arcpy
import time
import sys
import os

time_start = time.time()


def main():

    print("\nThis program asks a user to enter the directory name")
    print("for the 'Redlands.gdb' geodatabase. Users have 3 chances")
    print("to enter the correct directory before the program terminates.")
    print("If the correct information is entered, the GDB name,")
    print("contents, directory name, number of feature datasets, feature classes")
    print("(their shape type and number of records) are examined and printed.")
    print("Finally, it writes the output information to a .txt file")

    # Setting the workspace and file out name/location

    arcpy.env.workspace = r"C:\GISc450\ArcPy4_GDB\Redlands.gdb"
    # workspace_no_caps = r"c:\gisc450\arcpy4_gdb\redlands.gdb"
    file_out = "Strobel_Noah_Output.txt"

    # Creating the input functions for the user to enter the GDB file directory info

    gdb_input = input("\nPlease enter the full geodatabase file directory name. You have 3\n"
                      "chances before the program terminates. Capitalization is not necessary: ")

    exists = os.path.exists(gdb_input)
    count = 0

    while not exists:
        gdb_input = input("\nYour entry is not recognized. Please try again: ")
        exists = os.path.exists(gdb_input)
        count += 1
        if count == 2:
            print("\nThe geodatabse could not be located and the")
            print("program has ended. To start over, click 'run'")
            return

    if gdb_input == arcpy.env.workspace or gdb_input == workspace_no_caps:
        print("\nThe geodatabase has been located. Printing its contents...")

    # Setting up variables to print the GDB info

    gdb_name = (arcpy.env.workspace[22:34])
    gdb_directory = arcpy.env.workspace
    fc_count = len(arcpy.ListFeatureClasses())

    print("\n=================================================================")
    print(f"File geodabase name: {gdb_name}")
    print(f"File geodatabase directory: {gdb_directory}")
    print(f"File geodatabase contains {fc_count} feature datasets")

    # Starting to examine the Redlands.gdb feature datasets and feature classes

    datasets = arcpy.ListDatasets()

    for ds in datasets:
        ds_desc = arcpy.Describe(ds)
        ds_name = ds_desc.name
        print(f"\n{ds_name}")
        fc_list = arcpy.ListFeatureClasses(feature_dataset=ds)
        for fc in fc_list:
            tables = (arcpy.ListTables())
            desc = arcpy.Describe(fc)
            shape_type = desc.shapeType
            get_count = arcpy.GetCount_management(fc)
            count = int(get_count.getOutput(0))

            print(f"\t{fc} is a {shape_type} feature containing {count} records")

    # Examining the file geodatabase table (DonutShops) info and printing it

    for table in tables:
        table_get_count = arcpy.GetCount_management(table)
        table_count = int(table_get_count.getOutput(0))

        print(f"{table} is a file geodatabase table containing {table_count} records")

    # Examining the feature classes info and printing it

    fc_names = arcpy.ListFeatureClasses()
    for fc in fc_names:
        fc_desc = arcpy.Describe(fc)
        fc_name = fc_desc.name
        fc_shape_type = fc_desc.shapeType
        fc_get_count = arcpy.GetCount_management(fc)
        fc_count = int(fc_get_count.getOutput(0))

        print(f"{fc_name} is a {fc_shape_type} feature containing {fc_get_count} records")
    print("=================================================================")

    # Creating the output .txt file. If it already exists, it will be deleted and re-written

    if arcpy.Exists(file_out):
        arcpy.Delete_management(file_out)
        open(file_out, "x")

    # Sending/writing the above info to our newly-created .txt file. The info here
    # is the same as above

    sys.stdout = open(file_out, "w")

    print("\nThis program asks a user to enter the directory name")
    print("for the 'Redlands.gdb' geodatabase. Users have 3 chances")
    print("to enter the correct directory before the program terminates.")
    print("If the correct information is entered, the GDB name,")
    print("contents, directory name, number of feature datasets, feature classes")
    print("(their shape type and number of records) are examined and printed.")
    print("Finally, it writes the output information to a .txt file")

    print("\n=================================================================")

    print(f"File geodabase name: {gdb_name}")
    print(f"File geodatabase directory: {gdb_directory}")
    print(f"File geodatabase contains {fc_count} feature datasets")

    datasets = arcpy.ListDatasets()

    for ds in datasets:
        ds_desc = arcpy.Describe(ds)
        ds_name = ds_desc.name
        print(ds_name)
        fc_list = arcpy.ListFeatureClasses(feature_dataset=ds)
        for fc in fc_list:
            tables = (arcpy.ListTables())
            desc = arcpy.Describe(fc)
            shape_type = desc.shapeType
            get_count = arcpy.GetCount_management(fc)
            count = int(get_count.getOutput(0))

            print(f"\t{fc} is a {shape_type} feature containing {count} records")

    for table in tables:
        table_get_count = arcpy.GetCount_management(table)
        table_count = int(table_get_count.getOutput(0))

        print(f"{table} is a file geodatabase table containing {table_count} records")

    fc_names = arcpy.ListFeatureClasses()
    for fc in fc_names:
        fc_desc = arcpy.Describe(fc)
        fc_name = fc_desc.name
        fc_shape_type = fc_desc.shapeType
        fc_get_count = arcpy.GetCount_management(fc)
        fc_count = int(fc_get_count.getOutput(0))
        print(f"{fc_name} is a {fc_shape_type} feature containing {fc_get_count} records")
    print("=================================================================")


if __name__ == '__main__':
    main()

# Timing the script's run time. Info is printed to the .txt file

time_end = time.time()
total_time = time_end - time_start
minutes = int(total_time / 60)
seconds = total_time % 60
print(f"\nThe script finished in {minutes} minutes {int(seconds)} seconds")

# Closing the output file

sys.stdout.close()

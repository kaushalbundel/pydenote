# How to think about making this project?

- Create separate files for each function that program should do and create individual modules for them
- Collate these individual modules into a single package once all the features are developed

## Features of the program

- The programs helps in defining the name of the file and creating the file for further note taking. Usually the naming of things is the most complicated aspect of the programming. This problem has been solved by using a standard template which is quite intuitive and it makes very convenient to retrieve files using simple command line tools such as grep.
  - The nomenclature builds on Three components:
    - Date: The starting point of the file is centered around dates so that the notes can be sorted by dates.
    - Name of the file: The name associated with the file. It could be anything that the user suggests
    - tags: Tags are meant for easy retrieval, wherein the user can recall or group the notes using their tags.
      - The tags should be stored somewhere in the memory to avoid duplication. The user should be also able to view the tags that they have already used so as to avoid duplication.
- UI: The program will be a command line tool that will have some preset questions which will help the user to create the file with the desired name
  - Questions:
    - Enter name of file?
      - At this time the user can view the file that they have already created, the list of file names can get shorter as the user is typing a file name.
    - Enter the file tags?
      - At this time the user can view the file tags that they have already used. The file tags can be added in a comma separated fashion. The new file tags will get appended to the file tag list.
- Output: The user will get a confirmation that the file has been created with the desired name (Combination of date, name and tags). The file will be a markdown file.
  - In the next version I can perhaps provide another option to the user for creating either a markdown file or a txt file.
  - I can also prepend the title of the note and the tags to the note itself.

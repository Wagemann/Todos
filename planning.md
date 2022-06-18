# Feature 3 Project Model [x] 

    [x] name - string - max char 200
    [x] description - string - no max length
    [x] members - many to many refers to auth user model

    [x] __str__ for name property

# Feature 4 Model to Admin [x]

    [x] Register Project Model to Admin

# Feature 5 List View for Project Model
* This feature is about creating a list view for the Project model, registering the view for a path, registering the projects paths with the tracker project, and creating a template for the view.

        [ ] Create a view that will get all instances of the project model and puts them in the context for the template
        [ ] Register view in projects app for the path "" and the name "list_project" in NEW FILE projects/urls.py
        [ ] Include Url patterns from projects app in the tracker project with the prefix "projects/"
        [ ] Create a template for the list view

## Template Specs [ ]

    [ ] Extend Base Html
    [ ] Div
        [ ] H1 - My Projects
        [ ] p tag - You are not assigned to any projects
        *if no projects p tag
        [ ] a table that has two columns
            [ ] Header Name rows with names of projects
            [ ] Number of tasks   


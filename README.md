# Google-Form-Management
SSL PROJECT

Clone the repository on the machine using git clone or download ZIP
Inside the directory installed run:
$python manage.py runserver

The URL generated will be the link to the product. You can sign up/ login and then create your own forms/change password/edit profile/
create questions of modular kind in your form.

THe link generated for forms can be shared by you for people to fill in. And the responses will be stored and you can click on 
"Export CSV" to see them in csv file ( view responses) or also visualize data in the form of pie chart/bar graphs.

You can add collabarators to your form too.

Conditional forms feature is there by which you can ask for options in form only if some options have been selected in a particular way.

Form Validation feature allows you to be specefic about needed responses, Example:
  ->Numeric
  ->EMail
  ->.pdf extension
  ->Alphanumeric

For database details you can go to db.sqlite3 and see relevant tables.

We have 2 tables:
a)One with Form ID and User ID
b)One with Form ID and Questions with all its info (Required/Not, Visible/Not, Text, Type, Choice)

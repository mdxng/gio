
from flask_wtf import FlaskForm
from wtforms.fields import HiddenField, StringField, DateField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length

#event form

class CreateEventForm(FlaskForm):  
    #Delete
    method = HiddenField()
    id = HiddenField()

    #Event
    title = StringField(validators=[InputRequired(), Length(min=1)]) 
    date = DateField(validators=[InputRequired()])
    submit = SubmitField('Create')

    #To Do
    check = BooleanField()
    toDo = StringField(validators=[Length(min=1)])
    toDoSubmit = SubmitField('Add')

    #Comment
    comment = TextAreaField(validators=[Length(min=1)])
    commentSubmit = SubmitField('Comment')






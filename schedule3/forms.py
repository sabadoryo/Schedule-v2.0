from django import forms


class SearchForm(forms.Form):
    search_string = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "searchTerm basicAutoComplete", 'placeholder': 'Группа,преподаватель,кабинет',
                   'data-url': "ajax/search_autocomplete", 'data-noresults-text': "Nothing to see here."}))

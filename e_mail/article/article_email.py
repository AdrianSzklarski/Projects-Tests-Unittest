class Email:
    """ A simple class that describe
    number of scientific articles, article credits and author contact"""

    def __init__(self, articles, points, name, surname):
        self.articles = articles
        self.points = points
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    @property
    def get_contact_author_name(self):
        return f'{self.name.lower().title()}.{self.surname.lower().title()}@gmail.com'

    @property
    def get_points_of_articles(self):
        points = round(self.articles * self.points, 2)
        return points

    def publication_bonus(self):
        points = self.get_points_of_articles
        return round((points*0.25+points), 2)

if __name__ == '__main__':
    Name = input('Give name: ')
    Surname = input('Give surname: ')
    article = Email(123, 25, Name, Surname)
    print(article.get_contact_author_name)
    print('Points for articles & bonus: ', article.get_points_of_articles, '&', article.publication_bonus())
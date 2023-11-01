$.get("https://swapi-api.alx-tools.com/api/films/?format=json", (date) => {
  films = date.results;
  for (film of films) {
    $("#list_movies").append("<li>" + film.title + "</li>");
  }
});

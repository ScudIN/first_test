def profile(name, age, *language):
 print(name, age, end=" ")
 for lang in language:
  print(lang, end=" ")
 print()
profile("유재석", 20, "Python", "Java", "C", "C#", "C++", "JS")
profile("김태호", 20, "Swift", "Kotlin")
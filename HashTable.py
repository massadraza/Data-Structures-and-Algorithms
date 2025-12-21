# Hash Table implementation in python
# Lookups can take place in O(1) but if there are hash collisions, it can take O(n) time
# The keys are hashed into a value which allows for O(1) lookup

grades = {
    'John': 60, 
    'Bob': 70,
    'Jack': 100,
    'Mike': 20,

}

print(grades['John'])
print(grades['Bob'])
print(grades)

# A set is also a hash map but it only stores keys
# Still, we have O(1) lookup since keys are hashed but we still may have an issue when there are hash collisions

setStudents = {'John', 'Bob', 'Jack', 'Mike'}
setStudents.add('Donald')

print('John' in setStudents)
print('Michael' in setStudents)
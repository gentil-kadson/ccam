class PersonFilterSet:
    class Meta:
        fields = {
            "person__registration": ["contains"],
            "person__email": ["contains"],
            "person__name": ["icontains"],
            "person__cpf": ["contains"],
        }

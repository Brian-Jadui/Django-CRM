from django.test import TestCase

# Create your tests here.
            <form class="form" method="POST" action="{% url 'edit-account' %}" enctype="multipart/form-data">
                {% csrf_token %}
                {% for field in form %}
                <div class="form__field">
                    <label for="formInput#text">{{field.label}}</label>
                    {{field}}
                </div>
                {% endfor %}
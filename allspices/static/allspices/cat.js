document.addEventListener('DOMContentLoaded', function(){
    
    //Us button to toggle between categories
    document.getElementById("Break_view").addEventListener('click', load_break);
    document.getElementById("Lunch_view").addEventListener('click', load_lunch);
    document.getElementById("Dinner_view").addEventListener('click', load_dinner);
    document.getElementById("Dessert_view").addEventListener('click', load_dessert);
    document.getElementById("Beverages_view").addEventListener('click', load_beverages);
    document.getElementById("Salads_view").addEventListener('click', load_salads);

    //By default, load Breakfast
    load_break();
});

function load_break() {
    document.getElementById("Breakfast").style.display = 'block';
    document.getElementById("Lunch").style.display = 'none';
    document.getElementById("Dinner").style.display = 'none';
    document.getElementById("Desserts").style.display = 'none';
    document.getElementById("Beverages").style.display = 'none';
    document.getElementById("Salads").style.display = 'none';
}

function load_lunch() {
    document.getElementById("Lunch").style.display = 'block';
    document.getElementById("Breakfast").style.display = 'none';
    document.getElementById("Dinner").style.display = 'none';
    document.getElementById("Desserts").style.display = 'none';
    document.getElementById("Beverages").style.display = 'none';
    document.getElementById("Salads").style.display = 'none';
}

function load_dinner() {
    document.getElementById("Dinner").style.display = 'block';
    document.getElementById("Breakfast").style.display = 'none';
    document.getElementById("Lunch").style.display = 'none';
    document.getElementById("Desserts").style.display = 'none';
    document.getElementById("Beverages").style.display = 'none';
    document.getElementById("Salads").style.display = 'none';
}

function load_beverages() {
    document.getElementById("Beverages").style.display = 'block';
    document.getElementById("Breakfast").style.display = 'none';
    document.getElementById("Lunch").style.display = 'none';
    document.getElementById("Dinner").style.display = 'none';
    document.getElementById("Desserts").style.display = 'none';
    document.getElementById("Salads").style.display = 'none';
}

function load_salads() {
    document.getElementById("Salads").style.display = 'block';
    document.getElementById("Breakfast").style.display = 'none';
    document.getElementById("Lunch").style.display = 'none';
    document.getElementById("Dinner").style.display = 'none';
    document.getElementById("Desserts").style.display = 'none';
    document.getElementById("Beverages").style.display = 'none';
}

function load_dessert() {
    document.getElementById("Desserts").style.display = 'block';
    document.getElementById("Breakfast").style.display = 'none';
    document.getElementById("Lunch").style.display = 'none';
    document.getElementById("Dinner").style.display = 'none';
    document.getElementById("Beverages").style.display = 'none';
    document.getElementById("Salads").style.display = 'none';
}
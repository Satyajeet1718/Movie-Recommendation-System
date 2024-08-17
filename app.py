import tkinter as tk
from tkinter import messagebox
from src.recommender import MovieRecommender

# Initialize the recommender
recommender = MovieRecommender('data/credits.csv', 'data/movies.csv')

def get_recommendations():
    movie_title = entry.get()
    if not movie_title:
        messagebox.showwarning("Input Error", "Please enter a movie title.")
        return
    recommendations = recommender.recommend_movies(movie_title)
    if not recommendations:
        messagebox.showinfo("No Recommendations", f"No recommendations found for '{movie_title}'.")
    else:
        recommendations_list.delete(0, tk.END)
        for rec in recommendations:
            recommendations_list.insert(tk.END, rec)

# Set up the Tkinter window with dark theme
root = tk.Tk()
root.title("Movie Recommendation System")
root.configure(bg='#1e1e1e')  # Set background color

frame = tk.Frame(root, bg='#1e1e1e')
frame.pack(pady=20)

# Label for movie title entry
label = tk.Label(frame, text="Enter Movie Title:", bg='#1e1e1e', fg='#ffffff')
label.pack(side=tk.LEFT)

# Entry for movie title
entry = tk.Entry(frame, width=50, bg='#2d2d2d', fg='#ffffff', insertbackground='#ffffff')
entry.pack(side=tk.LEFT, padx=10)

# Button to get recommendations
recommend_button = tk.Button(frame, text="Get Recommendations", command=get_recommendations, bg='#007acc', fg='#ffffff', activebackground='#005f99', activeforeground='#ffffff')
recommend_button.pack(side=tk.LEFT)

# Listbox to display recommendations
recommendations_list = tk.Listbox(root, width=80, height=15, bg='#2d2d2d', fg='#ffffff', selectbackground='#3a3d41', selectforeground='#ffffff')
recommendations_list.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

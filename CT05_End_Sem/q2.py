
try:
    
    with open('reviews.txt', 'r') as file:
        lines = file.readlines()
    
    
    full_text = "".join(lines)
    total_chars = len(full_text)
    
    good_count = 0
    bad_count = 0
    total_reviews = len(lines)

    
    for review in lines:
        review_lower = review.lower()
        if "good" in review_lower:
            good_count += 1
        if "bad" in review_lower:
            bad_count += 1

    
    if total_reviews > 0:
        percentage_good = (good_count / total_reviews) * 100
    else:
        percentage_good = 0.0

    
    if percentage_good >= 70:
        rating = "Positive"
    elif 40 <= percentage_good < 70:
        rating = "Mixed"
    else:
        rating = "Negative"

    
    output = (
        f"Review Text Analysis\n"
        f"{'-' * 30}\n"
        f"Total Characters: {total_chars}\n"
        f"Good Reviews: {good_count}\n"
        f"Bad Reviews: {bad_count}\n"
        f"Percentage of Good Reviews: {percentage_good:.2f}%\n"
        f"Overall Rating: {rating}"
    )

    
    print(output)

    
    with open('review_results.txt', 'w') as out_file:
        out_file.write(output)

except FileNotFoundError:
    print("Error: reviews.txt not found. Please place the file in the root folder.")
def minutes_to_hours_and_minutes(minutes):
    # Calculate hours and remaining minutes
    hours = int(minutes // 60)
    remaining_minutes = int(minutes % 60)

    # Output the result
    print(f"Hours:{hours}\nMinutes: {remaining_minutes}\n")

# Example usage
input_minutes = float(input("Enter the minutes: "))
minutes_to_hours_and_minutes(input_minutes)
input("Press any key to exit...")

import React, { useState } from "react";
import "./HomePage.css";

const HomePage = () => {
  const [resultMessage, setResultMessage] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {
      month: formData.get("month"),
      hour: formData.get("hour"),
      minute: formData.get("minute"),
      day_of_week: parseInt(formData.get("day_of_week")),
      station: formData.get("station"),
      line: formData.get("line"),
      bound: formData.get("bound"),
    };

    const response = await fetch("http://localhost:5000/api/delay", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    const { delayProb, ifDelay } = result;

    const message = ifDelay
      ? `Yes, there will be a delay with a probability of ${delayProb}`
      : `No, there is no possible delay with a probability of ${delayProb}`;

    setResultMessage(message);
  };

  return (
    <div className="form-container">
      <h2>TTC Delay Information</h2>
      <form onSubmit={handleSubmit} method="post">
        <label htmlFor="month">Month:</label>
        <input
          type="number"
          id="month"
          name="month"
          min="1"
          max="12"
          required
        />

        <label htmlFor="hour">Hour:</label>
        <input type="number" id="hour" name="hour" min="0" max="23" required />

        <label htmlFor="minute">Minute:</label>
        <input
          type="number"
          id="minute"
          name="minute"
          min="0"
          max="59"
          required
        />

        <label htmlFor="day_of_week">Day of the Week:</label>
        <select id="day_of_week" name="day_of_week" required>
          <option value="0">Sunday</option>
          <option value="1">Monday</option>
          <option value="2">Tuesday</option>
          <option value="3">Wednesday</option>
          <option value="4">Thursday</option>
          <option value="5">Friday</option>
          <option value="6">Saturday</option>
        </select>

        <label htmlFor="station">Station:</label>
        <input type="text" id="station" name="station" required />

        <label htmlFor="line">Line:</label>
        <input type="text" id="line" name="line" required />

        <label htmlFor="bound">Bound:</label>
        <input type="text" id="bound" name="bound" required />

        <button type="submit">Submit</button>
      </form>
      {resultMessage && <p className="result-message">{resultMessage}</p>}
    </div>
  );
};

export default HomePage;

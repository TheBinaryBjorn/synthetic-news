"use client";
import { useState, useEffect } from "react";

export default function DarkLightSwitch() {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    const isDarkStored = localStorage.getItem("theme") === "dark";
    document.documentElement.classList.toggle("dark", isDarkStored);
    setIsDark(isDarkStored);
  }, []);

  const toggleTheme = () => {
    const newTheme = !isDark;
    setIsDark(newTheme);
    document.documentElement.classList.toggle("dark", newTheme);
    localStorage.setItem("theme", newTheme ? "dark" : "light");
  };

  return <button onClick={toggleTheme}>{isDark ? "Dark" : "Light"}</button>;
}

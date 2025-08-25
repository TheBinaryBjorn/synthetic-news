import { render, screen } from "@testing-library/react";
import Home from "@/app/page";

test("renders hello world", () => {
  render(<Home />);
  expect(screen.getByText("Hello World!")).toBeInTheDocument();
});

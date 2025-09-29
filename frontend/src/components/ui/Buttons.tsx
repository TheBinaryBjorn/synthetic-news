
import { ReactNode } from "react";

interface RoundedButtonProps {
  children: ReactNode;
  onClick?: () => void;
}

export function RoundedButton({ children, onClick }: RoundedButtonProps) {
  return (
    <button
      className="shadow-md p-2 bg-white/1 backdrop-blur-xl rounded-full text-white hover:bg-white/30 hover:cursor-pointer duration-300 transition-all"
      onClick={onClick}
    >
      {children}
    </button>
  );
}
"use client"
import { RoundedButton } from "../ui/Buttons";
import { useState } from "react";
import Image from "next/image";
import { User } from "lucide-react";
export default function ProfileButton() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [loggedInUser, setLoggedInUser] = useState(null);
  return (
    <RoundedButton>
      {isLoggedIn ? <Image src={loggedInUser.profilePicture} width={64} height={64} alt="Profile Picture"/> : <User/>}
    </RoundedButton>
  );
}

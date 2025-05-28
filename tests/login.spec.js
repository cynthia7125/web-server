import { test, expect } from '@playwright/test';
import { faker } from '@faker-js/faker';


test('has login and sign up', async ({ page }) => {
  await page.goto("http://localhost:8503");

  await expect(page).toHaveTitle(/Meme Clock/);
  await page.getByText("Signup").click();
  await page.getByText("Username").isVisible();
  const isButtonVisible = await page
    .getByText("Login")
    .isVisible();
  expect(isButtonVisible).toBe(true); 

});

test("Login happy flow", async ({ page }) => {
  await page.goto("http://localhost:8503");

  const randomUser = `user${faker.internet.username()}`;
  const randomEmail = `user${faker.internet.email()}`;
  const randomPass = `user${faker.internet.password()}`;

  await page.getByText("Signup").click();
  await page.getByRole("textbox", { name: "Username" }).fill(randomUser);
  await page.getByRole("textbox", { name: "Email" }).fill(randomEmail);
  await page
    .getByRole("textbox", { name: "Password" })
    .fill(randomPass);
  await page.getByRole("button", { name: "Sign Up" }).click();

  await page.waitForLoadState("networkidle");
  const welcome = await page.getByText("👋 Welcome, " + randomUser).isVisible();
  await expect(welcome).toBe(true);

  await page.getByRole("button", { name: "Logout" }).click();

  await page.getByRole("textbox", { name: "Email" }).fill(randomEmail);
  await page.getByRole("textbox", { name: "Password" }).fill(randomPass);
  await page.getByRole("button", { name: "Log in" }).click();

  await expect(welcome).toBe(true);

});

test("Login error flow", async ({ page }) => {
  await page.goto("http://localhost:8503");
  // Login with no password or email
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByTestId("stAlertContentError")).toBeVisible();
  await expect(await page.getByTestId("stAlertContentError")).toHaveText(
    "Email is required"
  );

  // Login with no password
  await page.reload();
  await page.getByRole("textbox", { name: "Email" }).fill(faker.internet.email());
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByTestId("stAlertContentError")).toBeVisible();
  await expect(await page.getByTestId("stAlertContentError")).toHaveText(
    "Password is required"
  );

  // Login with no email
  await page.reload();
  await page.getByRole("textbox", { name: "Password" }).fill(faker.internet.password());
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByTestId("stAlertContentError")).toBeVisible();
  await expect(page.getByTestId("stAlertContentError")).toHaveText(
    "Email is required"
  );

  // Login without first signing up
  await page.reload();
  await page.getByRole("textbox", { name: "Email" }).fill(faker.internet.email());
  await page.getByRole("textbox", { name: "Password" }).fill(faker.internet.password());
  await page.getByRole("button", { name: "Log in" }).click();
  await expect(page.getByTestId("stAlertContentError")).toBeVisible();
  const err = await page.getByTestId("stAlertContentError");
  await expect(err).toHaveText("Invalid email or password.");
});


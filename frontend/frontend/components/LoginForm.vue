<template>
  <div class="mx-auto flex w-full max-w-sm flex-col">
    <div class="mx-auto flex lg:hidden">
      <NuxtLogo />
    </div>
    <h1 class="mt-8 text-2xl font-semibold text-gray-700 lg:mt-0">
      Welcome back
    </h1>
    <p class="mt-2 text-sm text-gray-400">Please sign in below</p>
    <p class="mt-5 text-sm font-semibold text-gray-500">Email</p>
    <input class="mt-1 rounded border py-1 px-3 text-sm shadow" />
    <p class="mt-5 text-sm font-semibold text-gray-500">Password</p>
    <input
      class="mt-1 rounded border py-1 px-3 text-sm text-sm shadow"
      type="password"
    />
    <div class="mt-5 flex items-center">
      <input class="mr-2 align-middle text-sm text-sm" type="checkbox" />
      <p class="text-sm font-semibold text-gray-500">Remember me</p>
      <span class="flex-1" />
      <a
        href="#"
        class="text-sm font-semibold text-indigo-400 hover:text-indigo-500"
        >Forgot password?</a
      >
    </div>
    <button
      class="mt-5 rounded border bg-indigo-400 py-2 px-5 text-sm text-sm font-semibold text-gray-50 shadow hover:bg-indigo-500"
    >
      Sign in
    </button>
    <button
      class="mt-3 rounded border bg-white py-2 px-5 shadow hover:bg-gray-100"
    >
      <div class="flex items-center justify-center space-x-2">
        <GitHubLogo />
        <span class="text-sm font-semibold text-gray-700"
          >Sign in with GitHub</span
        >
      </div>
    </button>
    <div class="mt-8 flex items-center space-x-1">
      <p class="text-sm font-semibold text-gray-500">Don't have an account?</p>
      <a
        href="#"
        class="text-sm font-semibold text-indigo-400 hover:text-indigo-500"
        >Sign up</a
      >
    </div>
  </div>
</template>

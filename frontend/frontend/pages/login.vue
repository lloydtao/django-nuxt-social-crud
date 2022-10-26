<template>
  <div>
    <div class="flex">
      <div class="min-h-screen flex-1">
        <div class="flex h-full items-center py-8 px-5">
          <LoginForm />
        </div>
      </div>
      <div class="hidden min-h-screen flex-1 bg-gray-50 px-5 py-5 lg:flex">
        <div class="mx-auto flex h-full items-center">
          <NuxtLogo />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  layout: 'login',
}
</script>
